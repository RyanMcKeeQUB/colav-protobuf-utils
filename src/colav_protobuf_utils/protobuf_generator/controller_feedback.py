from colav_protobuf import ControllerFeedback
from enum import Enum

class CTRLMode(Enum):
    UNKNOWN = 0
    CRUISE = 1
    T2LOS = 2
    T2Theta = 3
    FB = 4
    WAYPOINT_REACHED = 5

class CTRLStatus(Enum):
    UNKOWN_STATUS = 0
    ACTIVE = 1
    INACTIVE = 2
    ERROR = 3

def gen_controller_feedback(
        mission_tag: str,
        agent_tag: str,
        ctrl_mode: CTRLMode,
        ctrl_status: CTRLStatus,
        velocity: float,
        yaw_rate: float,
        timestamp: str
):
    feedback = ControllerFeedback()
    feedback.mission_tag = mission_tag
    feedback.agent_tag = agent_tag
    feedback.ctrl_mode = ControllerFeedback.CTRLMode.Value(ctrl_mode.name)
    feedback.ctrl_status = ControllerFeedback.CTRLStatus.Value(ctrl_status.name)
    feedback.ctrl_cmd.velocity = velocity
    feedback.ctrl_cmd.yaw_rate = yaw_rate
    feedback.timestamp = timestamp
    return feedback
