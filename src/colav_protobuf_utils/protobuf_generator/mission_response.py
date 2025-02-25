from colav_protobuf import MissionResponse
from enum import Enum


class MissionResponseEnum(Enum):
    UNKOWN = 0
    MISSION_STARTING = 1
    MISSION_ERROR = 2
    MISSION_INVALID = 3


def gen_protobuf_mission_response(
    mission_tag: str,
    mission_start_timestamp: str,
    mission_respone_enum: MissionResponseEnum,
    mission_response_details: str,
) -> MissionResponse:
    """Generate a protobuf message for MissionResponse"""
    mission_response = MissionResponse()
    mission_response.mission_tag = mission_tag
    mission_response.mission_start_timestamp = mission_start_timestamp
    mission_response.mission_response = MissionResponse.MissionResponseEnum.Value(
        mission_respone_enum.name
    )
    mission_response.mission_response_details = mission_response_details

    return mission_response
