from colav_protobuf import MissionRequest
from colav_protobuf import MissionResponse
from colav_protobuf import ObstaclesUpdate
from colav_protobuf import AgentUpdate
from colav_protobuf import ControllerFeedback
from colav_protobuf_utils import ProtoType
from typing import Union


def serialize_protobuf(
    protobuf: Union[
        MissionRequest,
        MissionResponse,
        AgentUpdate,
        ObstaclesUpdate,
        ControllerFeedback,
    ]
) -> bytes:
    if not isinstance(
        protobuf,
        (
            MissionRequest,
            MissionResponse,
            AgentUpdate,
            ObstaclesUpdate,
            ControllerFeedback,
        ),
    ):
        raise TypeError("protobuf must be one of the defined types in the Union")

    try:
        return protobuf.SerializeToString()
    except Exception as e:
        raise Exception(f"Error serializing protobuf: {e}")
