from colav_protobuf.missionRequest_pb2 import MissionRequest
from colav_protobuf.missionResponse_pb2 import MissionResponse
from colav_protobuf.obstaclesUpdate_pb2 import ObstaclesUpdate
from colav_protobuf.agentUpdate_pb2 import AgentUpdate
from colav_protobuf.missionResponse_pb2 import MissionResponse
from colav_protobuf.controllerFeedback_pb2 import ControllerFeedback
from enum import Enum

class ProtoType(Enum):
    MISSION_REQUEST = "mission_request"
    MISSION_RESPONSE = "mission_response"
    AGENT_UPDATE = "agent_update"
    OBSTACLES_UPDATE = "obstacles_update"
    CONTROLLER_FEEDBACK = "controller_feedback"


def deserialise_protobuf(protobuf):
    """Generic Serialiszation function for colav protobuf messages"""
    raise TypeError(f"Unsupported protobuf type: {type(protobuf)}")

@deserialise_protobuf.register
def _(protobuf: bytes, type: ProtoType.MISSION_REQUEST) -> MissionRequest:
    try: 
        return protobuf.ParseFromString()
    except Exception as e:
        raise

@deserialise_protobuf.register
def _(protobuf: bytes, type: ProtoType.MISSION_RESPONSE) -> MissionResponse:
    try:
        return protobuf.ParseFromString()
    except Exception as e:
        raise

@deserialise_protobuf.register
def _(protobuf: bytes, type: ProtoType.AGENT_UPDATE) -> AgentUpdate: 
    try: 
        return protobuf.ParseFromString()
    except Exception as e: 
        raise e
    
@deserialise_protobuf.register
def _(protobuf: bytes, type: ProtoType.OBSTACLES_UPDATE) -> ObstaclesUpdate:
    try:
        return protobuf.ParseFromString()
    except Exception as e:
        raise e

@deserialise_protobuf.register
def _(protobuf: bytes, type: ProtoType.CONTROLLER_FEEDBACK) -> ControllerFeedback:
    try: 
        return protobuf.ParseFromString() 
    except Exception as e:
        raise e