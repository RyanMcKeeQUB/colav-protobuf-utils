from colav_protobuf import AgentUpdate
from enum import Enum
from typing import Tuple

def gen_agent_update(
    mission_tag: str,
    agent_tag: str,
    cartesian_position: Tuple[float, float, float],
    quaternium_orientation: Tuple[float, float, float, float],
    velocity: float,
    yaw_rate: float,
    acceleration: float,
    timestamp: str,
):
    """Generates a protobuf message for agent_update"""
    try:
        update = AgentUpdate()
        update.mission_tag = mission_tag
        update.agent_tag = agent_tag
        update.state.pose.position.x = cartesian_position[0]
        update.state.pose.position.y = cartesian_position[1]
        update.state.pose.position.z = cartesian_position[2]
        update.state.pose.orientation.x = quaternium_orientation[0]
        update.state.pose.orientation.y = quaternium_orientation[1]
        update.state.pose.orientation.z = quaternium_orientation[2]
        update.state.pose.orientation.w = quaternium_orientation[3]
        update.state.velocity = velocity
        update.state.yaw_rate = yaw_rate
        update.state.acceleration = acceleration
        update.timestamp = timestamp
    except Exception as e:
        raise Exception(e)

    return update