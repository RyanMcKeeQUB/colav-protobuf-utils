from colav_protobuf_utils.protobuf_generator import (
    gen_mission_response,
    MissionResponseTypeEnum,
)
from colav_protobuf.examples import mission_response


def test_proto_gen_mission_response():
    """pytest assertion tests for generation of protobuf mission response"""
    protogen_mission_response = gen_mission_response(
        tag=mission_response.tag,
        timestamp=mission_response.timestamp,
        response_type=MissionResponseTypeEnum(mission_response.response.type),
        response_details=mission_response.response.details,
    )
    assert protogen_mission_response.tag == mission_response.tag
    assert protogen_mission_response.timestamp == mission_response.timestamp
    assert protogen_mission_response.response.type == mission_response.response.type
    assert (
        protogen_mission_response.response.details == mission_response.response.details
    )
