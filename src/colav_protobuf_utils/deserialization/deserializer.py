from functools import singledispatch
from colav_protobuf.missionRequest_pb2 import MissionRequest
from colav_protobuf.missionResponse_pb2 import MissionResponse
from colav_protobuf.obstaclesUpdate_pb2 import ObstaclesUpdate
from colav_protobuf.agentUpdate_pb2 import AgentUpdate
from colav_protobuf.controllerFeedback_pb2 import ControllerFeedback
from enum import Enum


class ProtoType(Enum):
    MISSION_REQUEST = "mission_request"
    MISSION_RESPONSE = "mission_response"
    AGENT_UPDATE = "agent_update"
    OBSTACLES_UPDATE = "obstacles_update"
    CONTROLLER_FEEDBACK = "controller_feedback"


@singledispatch
def deserialise_protobuf(protobuf):
    """Generic deserialization function for colav protobuf messages"""
    raise TypeError(f"Unsupported protobuf type: {type(protobuf)}")


@deserialise_protobuf.register
def _(protobuf: bytes) -> MissionRequest:
    msg = MissionRequest()
    msg.ParseFromString(protobuf)
    return msg


@deserialise_protobuf.register
def _(protobuf: bytes) -> MissionResponse:
    msg = MissionResponse()
    msg.ParseFromString(protobuf)
    return msg


@deserialise_protobuf.register
def _(protobuf: bytes) -> AgentUpdate:
    msg = AgentUpdate()
    msg.ParseFromString(protobuf)
    return msg


@deserialise_protobuf.register
def _(protobuf: bytes):
    msg = ObstaclesUpdate()
    msg.ParseFromString(protobuf)
    return msg


@deserialise_protobuf.register
def _(protobuf: bytes):
    msg = ControllerFeedback()
    msg.ParseFromString(protobuf)
    return msg
