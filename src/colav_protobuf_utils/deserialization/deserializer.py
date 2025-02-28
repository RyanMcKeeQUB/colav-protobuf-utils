from functools import singledispatch
from colav_protobuf.missionRequest_pb2 import MissionRequest
from colav_protobuf.missionResponse_pb2 import MissionResponse
from colav_protobuf.obstaclesUpdate_pb2 import ObstaclesUpdate
from colav_protobuf.agentUpdate_pb2 import AgentUpdate
from colav_protobuf.controllerFeedback_pb2 import ControllerFeedback
from colav_protobuf_utils.protobuf_generator.mission_request import VesselType
from enum import Enum
import math


class ProtoType(Enum):
    MISSION_REQUEST = "mission_request"
    MISSION_RESPONSE = "mission_response"
    AGENT_UPDATE = "agent_update"
    OBSTACLES_UPDATE = "obstacles_update"
    CONTROLLER_FEEDBACK = "controller_feedback"


@singledispatch
def deserialise_protobuf(protobuf):
    """Generic deserialization function for colav protobuf messages"""
    raise TypeError(f"Unsupported protobuf type: {type(protobuf)}")


# Define constants for error messages for easy maintenance
INVALID_MISSION_TAG_MSG = "MissionRequest tag is empty"
INVALID_MISSION_TIMESTAMP = "MissionRequest timestamp is empty"
INVALID_VESSEL_TAG_MSG = "MissionRequest vessel tag is empty"
INVALID_VESSEL_TYPE_MSG = "MissionRequest vessel type is invalid, Needs to be one of the values assigned in colav_protobuf_utils.protobuf_generator.mission_request.VesselType"
INVALID_CONSTRAINT_MSG = "MissionRequest vessel constraints, {} invalid"
INVALID_GEOMETRY_MSG = "MissionRequest vessel geometry, {} invalid"


# Reusable validation functions
def validate_constraints(constraints):
    if constraints.max_acceleration <= 0:
        raise ValueError(INVALID_CONSTRAINT_MSG.format("max_acceleration"))
    if constraints.max_deceleration <= 0:
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


@deserialise_protobuf.register
def _(protobuf: bytes) -> MissionRequest:
    try:
        msg = MissionRequest()
        msg.ParseFromString(protobuf)

        # Validation checks
        if not msg.tag:
            raise ValueError(INVALID_MISSION_TAG_MSG)
        if not msg.timestamp:
            raise ValueError(INVALID_MISSION_TIMESTAMP)

        if not msg.vessel.tag:
            raise ValueError(INVALID_VESSEL_TAG_MSG)

        if msg.vessel.type not in VesselType.values():
            raise ValueError(INVALID_VESSEL_TYPE_MSG)

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

    except ValueError as e:
        raise ValueError(f"deserializer::deserialise_protobuf: {e}")
    except Exception as e:
        # Log original exception before re-raising
        raise Exception(f"Unexpected error in deserialising protobuf: {e}")

    return msg


def _max_radius(beam: float, loa: float) -> float:
    """Calculate the diagonal of vessel geometry and return as min safety radius"""
    diagonal = math.sqrt(beam**2 + loa**2)
    return diagonal / 2


@deserialise_protobuf.register
def _(protobuf: bytes) -> MissionResponse:
    msg = MissionResponse()
    msg.ParseFromString(protobuf)
    return msg


@deserialise_protobuf.register
def _(protobuf: bytes) -> AgentUpdate:
    msg = AgentUpdate()
    msg.ParseFromString(protobuf)
    return msg


@deserialise_protobuf.register
def _(protobuf: bytes):
    msg = ObstaclesUpdate()
    msg.ParseFromString(protobuf)
    return msg


@deserialise_protobuf.register
def _(protobuf: bytes):
    msg = ControllerFeedback()
    msg.ParseFromString(protobuf)
    return msg
