# import pytest

# from colav_protobuf_utils.serialization.serializer import serialise_protobuf

# from colav_protobuf.examples import mission_request
# from colav_protobuf.examples import mission_response

# from colav_protobuf.examples import agent_update
# from colav_protobuf.examples import obstacles_update

# from colav_protobuf.examples import controller_feedback


# @pytest.mark.parametrize(
#     "message",
#     [
#         mission_request,
#         mission_response,
#         agent_update,
#         obstacles_update,
#         controller_feedback,
#     ],
# )
# def test_serialiser(message):
#     try:
#         serialise_protobuf(message)
#         assert True
#     except Exception:
#         assert False
