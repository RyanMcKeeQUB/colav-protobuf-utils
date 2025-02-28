import pytest

from colav_protobuf_utils.serialization.serializer import serialize_protobuf
from colav_protobuf_utils.deserialization.deserializer import deserialize_protobuf
from colav_protobuf.examples import mission_request
from colav_protobuf.examples import mission_response

from colav_protobuf.examples import agent_update
from colav_protobuf.examples import obstacles_update

from colav_protobuf.examples import controller_feedback

from colav_protobuf_utils import VesselType, ProtoType

PROTO_TYPE = ProtoType.MISSION_REQUEST


@pytest.mark.parametrize(
    "message",
    [
        serialize_protobuf(mission_request),
        # serialize_protobuf(mission_response),
        # serialize_protobuf(agent_update),
        # serialize_protobuf(obstacles_update),
        # serialize_protobuf(controller_feedback),
    ],
)
def test_deserialiser(message):
    try:
        deserialize_protobuf(message, PROTO_TYPE)
        assert True
    except Exception as e:
        print(f"Exception: {e}")
        assert False


# # def test_deserialiser_invalid_message():
# #     with pytest.raises(Exception):
# #         deserialise_protobuf(b"invalid message")
# @pytest.mark.parametrize(
#     "field",
#     [
#         "tag",
#         # "timestamp",
#         # "vessel.tag",
#         # "vessel.type",
#         # "vessel.constraints.max_acceleration",
#         # "vessel.constraints.max_deceleration",
#         # "vessel.constraints.max_velocity",
#         # "vessel.constraints.min_velocity",
#         # "vessel.constraints.max_yaw_rate",
#     ],
# )
# def test_mission_request_validation(field):

#     invalid_mission_request = setattr(mission_request, field, "")
#     serialised_invalid_msg = serialize_protobuf(invalid_mission_request)
#     print(deserialize_protobuf(proto=serialised_invalid_msg, proto_type=PROTO_TYPE))
#     raise Exception


# # def test_mission_response_validation():
# #     pass


# # def test_agent_update_validation():
# #     pass


# # def test_obstacles_update_validation():
# #     pass
