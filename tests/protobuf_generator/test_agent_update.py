from colav_protobuf_utils.protobuf_generator import gen_agent_update
from colav_protobuf.examples import agent_update
import pytest


def get_cartesian_position(state):
    return [state.pose.position.x, state.pose.position.y, state.pose.position.z]


def get_quaternion_orientation(state):
    return [
        state.pose.orientation.x,
        state.pose.orientation.y,
        state.pose.orientation.z,
        state.pose.orientation.w,
    ]


def test_gen_agent_update():
    """pytest assertion tests for generation of protobuf agent update"""
    proto_utils_agent_update = gen_agent_update(
        mission_tag=agent_update.mission_tag,
        agent_tag=agent_update.agent_tag,
        cartesian_position=get_cartesian_position(agent_update.state),
        quaternium_orientation=get_quaternion_orientation(agent_update.state),
        velocity=agent_update.state.velocity,
        yaw_rate=agent_update.state.yaw_rate,
        acceleration=agent_update.state.acceleration,
        timestamp=agent_update.timestamp,
    )

    assert proto_utils_agent_update.mission_tag == agent_update.mission_tag
    assert proto_utils_agent_update.agent_tag == agent_update.agent_tag
    assert (
        proto_utils_agent_update.state.pose.position == agent_update.state.pose.position
    )
    assert (
        proto_utils_agent_update.state.pose.orientation
        == agent_update.state.pose.orientation
    )
    assert proto_utils_agent_update.state.velocity == agent_update.state.velocity
    assert proto_utils_agent_update.state.yaw_rate == agent_update.state.yaw_rate
    assert (
        proto_utils_agent_update.state.acceleration == agent_update.state.acceleration
    )
    assert proto_utils_agent_update.timestamp == agent_update.timestamp
