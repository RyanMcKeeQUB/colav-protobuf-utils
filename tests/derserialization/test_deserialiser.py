import pytest

from colav_protobuf_utils.serialization.serializer import serialize_protobuf
from colav_protobuf_utils.deserialization.deserializer import deserialize_protobuf
from colav_protobuf.examples import mission_request
from colav_protobuf.examples import mission_response

from colav_protobuf.examples import agent_update
from colav_protobuf.examples import obstacles_update

from colav_protobuf.examples import controller_feedback

from colav_protobuf_utils import VesselType, ProtoType
from colav_protobuf_utils.deserialization.deserializer import (
    INVALID_MISSION_TAG_MSG,
    INVALID_MISSION_TIMESTAMP_MSG,
    INVALID_VESSEL_TAG_MSG,
    INVALID_CONSTRAINT_MSG,
)

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


# def test_deserialiser_invalid_message():
#     with pytest.raises(Exception):
#         deserialise_protobuf(b"invalid message")
@pytest.mark.parametrize(
    "test, field, empty_value, exception_message",
    [
        ("empty missionRequest tag", "tag", "", INVALID_MISSION_TAG_MSG),
        (
            "empty missionRequest timestamp",
            "timestamp",
            "",
            INVALID_MISSION_TIMESTAMP_MSG,
        ),
        ("empty missionRequest vessel.tag", "vessel.tag", "", INVALID_VESSEL_TAG_MSG),
        (
            "empty missionRequest max acceleration",
            "vessel.constraints.max_acceleration",
            "None has type NoneType, but expected one of: int, float",
            INVALID_CONSTRAINT_MSG.format("max_acceleration"),
        ),
        (
            "empty missionRequest max_deceleration",
            "vessel.constraints.max_deceleration",
            None,
            "None has type NoneType, but expected one of: int, float",
        ),
        (
            "empty missionRequest max_velocity",
            "vessel.constraints.max_velocity",
            None,
            INVALID_CONSTRAINT_MSG.format("max_velocity"),
        ),
        (
            "empty missionRequest min_velocity",
            "vessel.constraints.min_velocity",
            None,
            INVALID_CONSTRAINT_MSG.format("min_velocity"),
        ),
        (
            "empty missionRequest max_yaw_rate",
            "vessel.constraints.max_yaw_rate",
            None,
            INVALID_CONSTRAINT_MSG.format("max_yaw_rate"),
        ),
        # "vessel.constraints.max_velocity",
        # "vessel.constraints.min_velocity",
        # "vessel.constraints.max_yaw_rate",
    ],
)
def test_invalid_mission_request_empty_fields(
    test, field, empty_value, exception_message
):

    invalid_mission_request = mission_request
    _set_nested_attr(invalid_mission_request, field, empty_value)

    with pytest.raises(ValueError) as excinfo:
        deserialize_protobuf(
            protobuf=serialize_protobuf(invalid_mission_request), proto_type=PROTO_TYPE
        )
    assert exception_message in str(excinfo.value)


def _set_nested_attr(obj, attr_path, value):
    """Set a nested attribute by traversing dot-separated fields."""
    attrs = attr_path.split(".")
    for attr in attrs[:-1]:  # Traverse until the second last attribute
        obj = getattr(obj, attr, None)
        if obj is None:
            raise AttributeError(f"Attribute '{attr}' not found in object.")

    setattr(obj, attrs[-1], value)  # Set the final attribute


# # def test_mission_response_validation():
# #     pass


# # def test_agent_update_validation():
# #     pass


# # def test_obstacles_update_validation():
# #     pass
