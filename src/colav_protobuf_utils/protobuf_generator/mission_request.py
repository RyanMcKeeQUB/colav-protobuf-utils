from colav_protobuf import MissionRequest
from typing import Tuple
from enum import Enum


class VesselType(Enum):
    UNSPECIFIED = 0
    HYDROFOIL = 1


def gen_mission_request(
    tag: str,
    timestamp: str,
    vessel_tag: str,
    vessel_type: VesselType,
    vessel_max_acceleration: float,
    vessel_max_deceleration: float,
    vessel_max_velocity: float,
    vessel_min_velocity: float,
    vessel_max_yaw_rate: float,
    vessel_loa: float,
    vessel_beam: float,
    vessel_safety_radius: float,
    cartesian_init_position: Tuple[float, float, float],
    cartesian_goal_position: Tuple[float, float, float],
    goal_safety_radius: float,
) -> MissionRequest:
    """Generates a protobuf message for MissionRequest"""
    req = MissionRequest()
    try:
        req.tag = tag
        req.timestamp = timestamp
        req.vessel.tag = vessel_tag
        req.vessel.type = MissionRequest.Vessel.VesselType.Value(vessel_type.name)
        req.vessel.constraints.max_acceleration = vessel_max_acceleration
        req.vessel.constraints.max_deceleration = vessel_max_deceleration
        req.vessel.constraints.max_velocity = vessel_max_velocity
        req.vessel.constraints.min_velocity = vessel_min_velocity
        req.vessel.constraints.max_yaw_rate = vessel_max_yaw_rate
        req.vessel.geometry.loa = vessel_loa
        req.vessel.geometry.beam = vessel_beam
        req.vessel.geometry.safety_radius = vessel_safety_radius
        req.init_position.x = cartesian_init_position[0]
        req.init_position.y = cartesian_init_position[1]
        req.init_position.z = cartesian_init_position[2]
        req.goal_waypoint.position.x = cartesian_goal_position[0]
        req.goal_waypoint.position.y = cartesian_goal_position[1]
        req.goal_waypoint.position.z = cartesian_goal_position[2]
        req.goal_waypoint.safety_radius = goal_safety_radius  # TODO: Change this to be acceptance radius instead of safety radius.
    except Exception as e:
        raise Exception(e)

    return req
