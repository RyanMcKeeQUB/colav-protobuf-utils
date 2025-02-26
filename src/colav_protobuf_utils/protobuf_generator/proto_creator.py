from colav_protobuf.missionRequest_pb2 import MissionRequest
from colav_protobuf.missionResponse_pb2 import MissionResponse

from colav_protobuf.obstaclesUpdate_pb2 import ObstaclesUpdate
from colav_protobuf.agentUpdate_pb2 import AgentUpdate
from typing import List
from enum import Enum

class CTRLMode(Enum):
    UNKOWN = 0
    CRUISE = 1
    T2LOS = 2
    T2Theta = 3
    FB = 4
    WAYPOINT_REACHED = 5


class CTRLStatus(Enum):
    pass


def gen_protobuf_controller_feedback(mission_tag: str, agent_tag: str, ctrl_mode: str):
    pass


@staticmethod
def _gen_state_common_vars(
    state, pose, velocity: float, yaw_rate: float, acceleration: float
):
    """Returns a common state"""
    state.pose = pose
    state.velocity = velocity
    state.yaw_rate = yaw_rate
    state.acceleration = acceleration

    return state


def gen_state(
    pose: AgentUpdate.Pose.Position,
    velocity: float,
    yaw_rate: float,
    acceleration: float,
):
    """Generate Agent State"""
    state = AgentUpdate.State()
    return _gen_state_common_vars(
        state=state,
        pose=pose,
        velocity=velocity,
        yaw_rate=yaw_rate,
        acceleration=acceleration,
    )


def gen_state(
    pose: ObstaclesUpdate.Pose.Position,
    velocity: float,
    yaw_rate: float,
    acceleration: float,
):
    state = ObstaclesUpdate.State()
    return _gen_state_common_vars(
        state=state,
        pose=pose,
        velocity=velocity,
        yaw_rate=yaw_rate,
        acceleration=acceleration,
    )
