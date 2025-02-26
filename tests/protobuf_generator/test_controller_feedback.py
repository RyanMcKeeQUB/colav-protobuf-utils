from colav_protobuf_utils.protobuf_generator import (
    gen_controller_feedback,
    CTRLMode,
    CTRLStatus,
)
from colav_protobuf.examples import controller_feedback
import pytest


def test_gen_controller_feedback():
    """pytest assertion tests for generation of protobuf controller feedback"""
    proto_utils_controller_feedback = gen_controller_feedback(
        mission_tag=controller_feedback.mission_tag,
        agent_tag=controller_feedback.agent_tag,
        ctrl_mode=CTRLMode(controller_feedback.ctrl_mode),
        ctrl_status=CTRLStatus(controller_feedback.ctrl_status),
        velocity=controller_feedback.ctrl_cmd.velocity,
        yaw_rate=controller_feedback.ctrl_cmd.yaw_rate,
        timestamp=controller_feedback.timestamp,
    )

    assert (
        proto_utils_controller_feedback.mission_tag == controller_feedback.mission_tag
    )
    assert proto_utils_controller_feedback.agent_tag == controller_feedback.agent_tag
    assert proto_utils_controller_feedback.ctrl_mode == controller_feedback.ctrl_mode
    assert (
        proto_utils_controller_feedback.ctrl_status == controller_feedback.ctrl_status
    )
    assert (
        proto_utils_controller_feedback.ctrl_cmd.velocity
        == controller_feedback.ctrl_cmd.velocity
    )
    assert (
        proto_utils_controller_feedback.ctrl_cmd.yaw_rate
        == controller_feedback.ctrl_cmd.yaw_rate
    )
    assert proto_utils_controller_feedback.timestamp == controller_feedback.timestamp
