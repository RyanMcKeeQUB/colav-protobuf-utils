from colav_protobuf_utils.protobuf_generator import gen_agent_update
from colav_protobuf.examples import agent_update
import pytest


def test_gen_agent_update():
    proto_utils_agent_update = gen_agent_update(
        mission_tag=agent_update.mission_tag,
        agent_tag=agent_update.agent_tag,
        cartesian_position=[
            agent_update.state.pose.position.x,
            agent_update.state.pose.position.y,
            agent_update.state.pose.position.z,
        ],
        quaternium_orientation=[
            agent_update.state.pose.orientation.x,
            agent_update.state.pose.orientation.y,
            agent_update.state.pose.orientation.z,
            agent_update.state.pose.orientation.w,
        ],
        velocity=agent_update.state.velocity,
        yaw_rate=agent_update.state.yaw_rate,
        acceleration=agent_update.state.acceleration,
        timestamp=agent_update.timestamp,
    )
    print(proto_utils_agent_update)


def main():
    test_gen_agent_update()


if __name__ == "__main__":
    main()
