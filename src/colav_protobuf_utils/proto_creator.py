from colav_protobuf.missionRequest_pb2 import MissionRequest
from colav_protobuf.missionResponse_pb2 import MissionResponse

from colav_protobuf.obstaclesUpdate_pb2 import ObstaclesUpdate
from colav_protobuf.agentUpdate_pb2 import AgentUpdate
from typing import List

@staticmethod
def gen_protobuf_mission_request(
    mission_tag: str, 
    mission_start_timestamp: str, 
    vessel: MissionRequest.Vessel, 
    init_position: MissionRequest.Point, 
    goal_position: MissionRequest.Point, 
    goal_acceptance_radius: float
) -> MissionRequest: 
    """Generates a protobuf message for MissionRequest"""
    mission_request = MissionRequest()
    try:
        mission_request.tag = mission_tag
        mission_request.mission_start_timestamp = mission_start_timestamp
        mission_request.vessel = vessel
        mission_request.init_position = init_position
        mission_request.goal_position = goal_position
        mission_request.mission_goal_acceptance_radius = goal_acceptance_radius

        return MissionRequest
    except Exception as e: 
        raise Exception(e)
    
from enum import Enum
class MissionResponseEnum(Enum):
    UNKOWN=0
    MISSION_STARTING=1
    MISSION_ERROR=2
    MISSION_INVALID=3
    
@staticmethod
def gen_protobuf_mission_response(
    mission_tag: str,
    mission_start_timestamp: str,
    mission_respone_enum: MissionResponseEnum,
    mission_response_details: str
) -> MissionResponse:
    mission_response = MissionResponse()
    mission_response.mission_tag = mission_tag
    mission_response.mission_start_timestamp = mission_start_timestamp
    mission_response.mission_response = MissionResponse.MissionResponseEnum.Value(mission_respone_enum.name)
    mission_response.mission_response_details = mission_response_details

    return mission_response


@staticmethod
def gen_protobuf_obstacles_update(
    mission_tag: str,
    dynamic_obstacles: List[ObstaclesUpdate.DynamicObstacle],
    static_obstacles: List[ObstaclesUpdate.StaticObstacle],
    timestamp: str, 
    timestep: str
)-> ObstaclesUpdate:
    """Generates a protobuf message for obstacles update"""
    try: 
        obstacles_update = ObstaclesUpdate()
        obstacles_update.mission_tag = mission_tag
        # need to do the repeated thing

        for idx, obstacle in enumerate(dynamic_obstacles): 
            obstacles_update.dynamic_obstacles.add()
            obstacles_update.dynamic_obstacles[idx] = obstacle

        for idx, obstacle in enumerate(static_obstacles):
            obstacles_update.static_obstacles.add()
            obstacles_update.static_obstacles[idx] = obstacle

        obstacles_update.timestamp = timestamp
        obstacles_update.timestep = timestep
    except Exception as e:
        raise Exception(e)

    return obstacles_update

def gen_protobuf_agent_update(
    mission_tag: str,
    agent_tag: str,
    state: AgentUpdate.State,
    timestamp: str,
    timestep: str
):
    """Generates a protobuf message for agent_update"""
    try:
        agent_update = AgentUpdate()
        agent_update.mission_tag = mission_tag
        agent_update.agent_tag = agent_tag
        agent_update.state = state
        agent_update.timestamp = timestamp
        agent_update.timestep = timestep
    except Exception as e:
        raise Exception(e)

    return agent_update

class CTRLMode(Enum):
    UNKOWN=0
    CRUISE=1
    T2LOS=2
    T2Theta=3
    FB=4
    WAYPOINT_REACHED=5

class CTRLStatus(Enum): 
    

def gen_protobuf_controller_feedback(
        mission_tag: str,
        agent_tag: str
        ctrl_mode: 
)

@staticmethod
def _gen_state_common_vars(state, pose, velocity: float, yaw_rate: float, acceleration: float):
    """Returns a common state"""
    state.pose = pose
    state.velocity = velocity
    state.yaw_rate = yaw_rate
    state.acceleration = acceleration

    return state

def gen_state(pose: AgentUpdate.Pose.Position, velocity: float, yaw_rate: float, acceleration: float):
    """Generate Agent State"""
    state = AgentUpdate.State()
    return _gen_state_common_vars(state=state, pose=pose, velocity=velocity, yaw_rate=yaw_rate, acceleration=acceleration)

def gen_state(pose: ObstaclesUpdate.Pose.Position, velocity: float, yaw_rate: float, acceleration: float):
    state = ObstaclesUpdate.State()
    return _gen_state_common_vars(state=state, pose=pose, velocity=velocity, yaw_rate=yaw_rate, acceleration=acceleration)
