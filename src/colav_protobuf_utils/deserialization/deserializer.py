from colav_protobuf import (
    MissionRequest,
    MissionResponse,
    AgentUpdate,
    ObstaclesUpdate,
    ControllerFeedback,
)
from colav_protobuf_utils import VesselType
from enum import Enum
import math
from typing import Union


class ProtoType(Enum):
    MISSION_REQUEST = "mission_request"
    MISSION_RESPONSE = "mission_response"
    AGENT_UPDATE = "agent_update"
    OBSTACLES_UPDATE = "obstacles_update"
    CONTROLLER_FEEDBACK = "controller_feedback"


# Define constants for error messages for easy maintenance
INVALID_MISSION_TAG_MSG = "MissionRequest tag is empty"
INVALID_MISSION_TIMESTAMP_MSG = "MissionRequest timestamp is empty"
INVALID_VESSEL_TAG_MSG = "MissionRequest vessel tag is empty"
INVALID_VESSEL_TYPE_MSG = "MissionRequest vessel type is invalid, Needs to be one of the values assigned in colav_protobuf_utils.protobuf_generator.mission_request.VesselType"
INVALID_CONSTRAINT_MSG = "MissionRequest vessel constraints, {} invalid"
INVALID_GEOMETRY_MSG = "MissionRequest vessel geometry, {} invalid"


# Reusable validation functions
def validate_constraints(constraints):
    if constraints.max_acceleration <= 0:
        raise ValueError(INVALID_CONSTRAINT_MSG.format("max_acceleration"))
    if constraints.max_deceleration >= 0:
        raise ValueError(INVALID_CONSTRAINT_MSG.format("max_deceleration"))
    if constraints.max_velocity <= 0:
        raise ValueError(INVALID_CONSTRAINT_MSG.format("max_velocity"))
    if (
        constraints.min_velocity <= 0
        or constraints.min_velocity >= constraints.max_velocity
    ):
        raise ValueError(INVALID_CONSTRAINT_MSG.format("min_velocity"))
    if constraints.max_yaw_rate <= 0 or constraints.max_yaw_rate >= 1:
        raise ValueError(INVALID_CONSTRAINT_MSG.format("max_yaw_rate"))


def validate_geometry(geometry):
    if not geometry.loa or geometry.loa < 0:
        raise ValueError(INVALID_GEOMETRY_MSG.format("loa"))
    if not geometry.beam or geometry.beam < 0:
        raise ValueError(INVALID_GEOMETRY_MSG.format("beam"))


def validate_waypoint(waypoint, vessel_geometry):
    if not waypoint.position:
        raise ValueError(
            "Mission request goal_waypoint.position must be given as a tuple of float representing cartesian coordinates of goal position."
        )
    if (
        not waypoint.safety_radius
        or _max_radius(beam=vessel_geometry.beam, loa=vessel_geometry.loa)
        < waypoint.safety_radius
    ):
        raise ValueError(
            f"MissionRequest goal_waypoint.safety radius must be given and it must be greater than or equal to max radius of geometry {_max_radius(beam=vessel_geometry.beam, loa=vessel_geometry.loa)}"
        )


def _max_radius(beam: float, loa: float) -> float:
    """Calculate the diagonal of vessel geometry and return as min safety radius"""
    diagonal = math.sqrt(beam**2 + loa**2)
    return diagonal / 2


def deserialize_protobuf(protobuf: bytes, proto_type: ProtoType):
    """deserialization dispatcher for colav protobuf messages"""
    try:
        if proto_type == ProtoType.MISSION_REQUEST:
            print("here")
            return _deserialize_mission_request(protobuf)
        if proto_type == ProtoType.MISSION_RESPONSE:
            return _deserialize_mission_response(protobuf)
        if proto_type == ProtoType.AGENT_UPDATE:
            return _deserialize_agent_update(protobuf)
        if proto_type == ProtoType.OBSTACLES_UPDATE:
            return _deserialize_obstacles_update(protobuf)
        if proto_type == ProtoType.CONTROLLER_FEEDBACK:
            return _deserialize_controller_feedback(protobuf)
    except ValueError as e:
        raise ValueError(f"deserializer::deserialise_protobuf: {e}")
    except Exception as e:
        raise Exception(
            f"deserializer::deserialise_protobuf: Unexpected Exception occured: {e}"
        )


def _deserialize_mission_request(protobuf: bytes) -> MissionRequest:
    """Deserialise MissionRequest protobuf message and validate its fields"""
    msg = MissionRequest()
    msg.ParseFromString(protobuf)

    print(msg)

    # Validation checks
    if not msg.tag:
        raise ValueError(INVALID_MISSION_TAG_MSG)
    if not msg.timestamp:
        raise ValueError(INVALID_MISSION_TIMESTAMP)
    if not msg.vessel.tag:
        raise ValueError(INVALID_VESSEL_TAG_MSG)
    if msg.vessel.type not in [
        MissionRequest.Vessel.VesselType.Value(type_.name) for type_ in VesselType
    ]:
        raise ValueError(INVALID_VESSEL_TYPE_MSG)
    print("Validating constraints")
    # Validate vessel constraints
    validate_constraints(msg.vessel.constraints)

    # Validate vessel geometry
    validate_geometry(msg.vessel.geometry)

    # Validate init position and goal waypoint
    if not msg.init_position:
        raise ValueError(
            "MissionRequest init_position must be given as a tuple of float representing cartesian coordinates"
        )
    validate_waypoint(msg.goal_waypoint, msg.vessel.geometry)

    return msg


def _deserialize_mission_response(protobuf: bytes) -> MissionResponse:
    """Deserialize MissionResponse protobuf message and validate its fields"""
    try:
        msg = MissionResponse()
        msg = msg.ParseFromString(protobuf)
    except Exception as e:
        raise Exception(
            f"deserializer::_deserialize_mission_response: Error deserializing MissionResponse: {e}"
        )
    return msg


def _deserialize_agent_update(protobuf: bytes) -> AgentUpdate:
    pass


def _deserialize_obstacles_update(protobuf: bytes) -> ObstaclesUpdate:
    pass


def _deserialize_controller_feedback(protobuf: bytes) -> ControllerFeedback:
    pass
