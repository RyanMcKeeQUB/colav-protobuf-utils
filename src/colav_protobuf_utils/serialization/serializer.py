from functools import singledispatch
from colav_protobuf import MissionRequest
from colav_protobuf import MissionResponse
from colav_protobuf import ObstaclesUpdate
from colav_protobuf import AgentUpdate
from colav_protobuf import ControllerFeedback


@singledispatch
def serialise_protobuf(protobuf) -> bytes:
    """Generic Serialization function for colav protobuf messages."""
    raise TypeError(f"Unsupported protobuf type: {type(protobuf)}")


@serialise_protobuf.register
def _(protobuf: MissionRequest) -> bytes:
    try:
        return protobuf.SerializeToString()
    except Exception as e:
        raise Exception(f"Error serializing MissionRequest: {e}")


@serialise_protobuf.register
def _(protobuf: MissionResponse) -> bytes:
    try:
        return protobuf.SerializeToString()
    except Exception as e:
        raise Exception(f"Error serializing MissionResponse: {e}")


@serialise_protobuf.register
def _(protobuf: AgentUpdate) -> bytes:
    try:
        return protobuf.SerializeToString()
    except Exception as e:
        raise Exception(f"Error serializing AgentUpdate: {e}")


@serialise_protobuf.register
def _(protobuf: ObstaclesUpdate) -> bytes:
    try:
        return protobuf.SerializeToString()
    except Exception as e:
        raise Exception(f"Error serializing ObstaclesUpdate: {e}")


@serialise_protobuf.register
def _(protobuf: ControllerFeedback) -> bytes:
    try:
        return protobuf.SerializeToString()
    except Exception as e:
        raise Exception(f"Error serializing ControllerFeedback: {e}")
