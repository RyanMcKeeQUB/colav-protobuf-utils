from colav_protobuf import MissionRequest
from typing import Tuple


def gen_mission_request(
    mission_tag: str,
    mission_start_timestamp: str,
    vessel: MissionRequest.Vessel,
    init_position: Tuple[float, float, float],
    goal_position: Tuple[float, float, float],
    goal_acceptance_radius: float,
) -> MissionRequest:
    """Generates a protobuf message for MissionRequest"""
    mission_request = MissionRequest()
    try:
        mission_request.tag = mission_tag
        mission_request.mission_start_timestamp = mission_start_timestamp
        mission_request.vessel = vessel
        mission_request.init_position = init_position
        mission_request.goal_position = goal_position
        mission_request.mission_goal_acceptance_radius = goal_acceptance_radius

        return MissionRequest
    except Exception as e:
        raise Exception(e)
