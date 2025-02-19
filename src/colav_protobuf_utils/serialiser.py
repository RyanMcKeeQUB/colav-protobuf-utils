from colav_protobuf.missionRequest_pb2 import MissionRequest
from colav_protobuf.missionResponse_pb2 import MissionResponse
from colav_protobuf.obstaclesUpdate_pb2 import ObstaclesUpdate
from colav_protobuf.agentUpdate_pb2 import AgentUpdate
from colav_protobuf.missionResponse_pb2 import MissionResponse
from colav_protobuf.controllerFeedback_pb2 import ControllerFeedback

def serialise_protobuf(protobuf) -> bytes:
    """Generic Serialiszation function for colav protobuf messages"""
    raise TypeError(f"Unsupported protobuf type: {type(protobuf)}")

@serialise_protobuf.register
def _(protobuf: MissionRequest) -> bytes:
    return protobuf.SerializeToString()

@serialise_protobuf.register
def _(protobuf: MissionResponse) -> bytes:
    return protobuf.SerializeToString()

@serialise_protobuf.register
def _(protobuf: AgentUpdate) -> bytes: 
    return protobuf.SerializeToString()

@serialise_protobuf.register
def _(protobuf: ObstaclesUpdate) -> bytes:
    return protobuf.SerializeToString()

@serialise_protobuf.register
def _(protobuf: MissionResponse) -> bytes:
    return protobuf.SerializeToString() 

@serialise_protobuf.register
def _(protobuf: ControllerFeedback) -> bytes:
    return protobuf.SerializeToString() 
    