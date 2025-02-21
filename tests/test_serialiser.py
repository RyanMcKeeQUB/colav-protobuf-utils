import pytest
from colav_protobuf.missionRequest_pb2 import MissionRequest
from colav_protobuf.missionResponse_pb2 import MissionResponse
from colav_protobuf.agentUpdate_pb2 import AgentUpdate
from colav_protobuf.obstaclesUpdate_pb2 import ObstaclesUpdate
from colav_protobuf.controllerFeedback_pb2 import ControllerFeedback

@pytest.fixture
def mock_mission_request():
    """mocks a mission request proto message"""
    mission_request = MissionRequest()
    # Mission metadata
    mission_request.tag = "COLAV_MISSION_NORTH_BELFAST_TO_SOUTH_FRANCE"
    mission_request.mission_start_timestamp = "1708353000" # UNIX timestamp (epoch time in seconds)
    
    # Static Vessel Information
    mission_request.vessel.tag = "EF12_WORKBOAT"
    mission_request.vessel.type = (
        MissionRequest.Vessel.VesselType.HYDROFOIL
    )
    mission_request.vessel.vessel_constraints.max_acceleration = 2.0
    mission_request.vessel.vessel_constraints.max_deceleration = -1.0
    mission_request.vessel.vessel_constraints.max_velocity = 30.0
    mission_request.vessel.vessel_constraints.min_velocity = 15.0
    mission_request.vessel.vessel_constraints.max_yaw_rate = 0.2
    mission_request.vessel.vessel_geometry.safety_threshold = 5
    
    # Earth-Centered, Earth-Fixed) Cartesian Coordinates North Belfast Lough in meters
    mission_request.mission_init_position.x = float(3,675,900.74)
    mission_request.mission_init_position.y = float(-372,412.13)
    mission_request.mission_init_position.z = float(5,181,577.70)

    # Earth-Centered, Earth-Fixed) Cartesian Coordinates South France near Marseille in meters WON'T USE THIS METRIC IN LOCAL MOTION PLANNER! GOOD FOR GLOBAL PLANNING
    mission_request.mission_goal_position.x = float(4680627.4)
    mission_request.mission_goal_position.z = float(503,374.5)
    mission_request.mission_goal_position.y = float(429,9351.3)
    # Need to change vessel and obstacle geometry to just consider length and breadth

    # Acceptance radius in meters of the goal waypoint for autonomous navigation.
    mission_request.mission_goal_acceptance_radius = float(5.0)

    return mission_request

@pytest.fixture
def mock_mission_response():
    """mocks a mission response proto message"""
    mission_response = MissionResponse()
    mission_response.mission_tag = "COLAV_MISSION_NORTH_BELFAST_TO_SOUTH_FRANCE"
    mission_response.mission_start_timestamp = "1708353005"
    mission_response.mission_response = MissionResponse.MissionResponseEnum.Value("MISSION_STARTING")
    mission_response.mission_response_details = "Mission has started. Now Navigating to South France"

@pytest.fixture
def mock_agent_update():
    """mocks a agent update proto message"""
    agent_update = AgentUpdate()
    agent_update.mission_tag = "COLAV_MISSION_NORTH_BELFAST_TO_SOUTH_FRANCE"
    agent_update.agent_tag = "EF12_WORKBOAT"
    agent_update.state.pose.position.x =   float(3,675,830.74)
    agent_update.state.pose.position.y = float(-272,412.13)
    agent_update.state.pose.position.z =  float(4,181,577.70)
    agent_update.state.pose.orientation.x = 0
    agent_update.state.pose.orientation.y = 0
    agent_update.state.pose.orientation.z = 0
    agent_update.state.pose.orientation.w = 1

    agent_update.state.velocity = 20
    agent_update.state.yaw_rate = 0.2
    agent_update.state.acceleration = 1

    agent_update.timestamp = "1708853235"
    agent_update.timestep = "000000000012331"

    return agent_update

@pytest.fixture
def mock_obstacles_update():
    """mocks a obstacles_update proto message"""
    obstacles_update = ObstaclesUpdate()

    return obstacles_update

@pytest.fixture
def mock_controller_feedback():
    """mocks a controller_feedback proto message"""
    controller_feedback = ControllerFeedback()
    controller_feedback.mission_tag = 'COLAV_MISSION_NORTH_BELFAST_TO_SOUTH_FRANCE'
    controller_feedback.agent_tag = 'EF12_WORKBOAT'
    controller_feedback.ctrl_mode = ControllerFeedback.CTRLMode.Value("CRUISE")
    controller_feedback.ctrl_status = ControllerFeedback.CTRLStatus.Value("ACTIVE")
    controller_feedback.ctrl_cmd.velocity = float(15.0)
    controller_feedback.ctrl_cmd.yaw_rate = float(0.2)

    controller_feedback.timestamp = "1708853235"
    controller_feedback.timestep = "000000000012331"

    return controller_feedback
