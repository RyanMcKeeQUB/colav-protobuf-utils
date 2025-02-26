import pytest

from colav_protobuf_utils.serialization.serializer import serialise_protobuf
from colav_protobuf_utils.deserialization.deserializer import deserialise_protobuf
from colav_protobuf.examples import mission_request
from colav_protobuf.examples import mission_response

from colav_protobuf.examples import agent_update
from colav_protobuf.examples import obstacles_update

from colav_protobuf.examples import controller_feedback


@pytest.mark.parametrize(
    "message",
    [
        serialise_protobuf(mission_request),
        serialise_protobuf(mission_response),
        serialise_protobuf(agent_update),
        serialise_protobuf(obstacles_update),
        serialise_protobuf(controller_feedback),
    ],
)
def test_deserialiser(message):
    try:
        deserialise_protobuf(message)
        assert True
    except Exception:
        assert False


def test_deserialiser_invalid_message():
    with pytest.raises(Exception):
        deserialise_protobuf(b"invalid message")
