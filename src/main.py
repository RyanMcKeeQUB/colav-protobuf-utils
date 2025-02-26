from colav_protobuf_utils.protobuf_generator import gen_mission_request, VesselType
from colav_protobuf_utils.protobuf_generator import gen_controller_feedback, CTRLStatus, CTRLMode
from colav_protobuf_utils.protobuf_generator import gen_agent_update

def test_mission_request_protogen_creator():
    return gen_mission_request(
        mission_tag="MOCK_MISSION",
        timestamp="000002000301",
        vessel_tag="MOCK_AGENTS",
        vessel_type=VesselType.HYDROFOIL,
        vessel_max_acceleration=float(5.0),
        vessel_max_deceleration=float(2.0),
        vessel_max_velocity=float(30),
        vessel_min_velocity=float(15.0),
        vessel_max_yaw_rate = float(0.2),
        vessel_loa = float(2.0),
        vessel_beam=float(0.5),
        vessel_safety_radius=float(2.0),
        cartesian_init_position=[float(0),float(0),float(0)],
        cartesian_goal_position=[float(0), float(0), float(0)],
        goal_acceptance_radius=float(15)
    )

def test_agent_update_protogen_creator():
    return gen_agent_update(
        mission_tag="MOCK_MISSION",
        agent_tag="MOCK_AGENT",
        cartesian_position=[0,0,0],
        quaternium_orientation=[0,0,0,1],
        velocity=15,
        yaw_rate=0.2,
        acceleration=0.2,
        timestamp="000012300"
    )

def test_controller_feedback_protogen_creator():
    return gen_controller_feedback(
        mission_tag="MOCK MISSION",
        agent_tag="mock agent",
        ctrl_mode=CTRLMode.CRUISE,
        ctrl_status=CTRLStatus.ACTIVE,
        velocity=float(15),
        yaw_rate=float(0.2),
        timestamp="0000012304"
    )

def main():
    proto_mission_request = test_mission_request_protogen_creator()
    print (proto_mission_request)

    proto_controller_feedback = test_controller_feedback_protogen_creator()
    print (proto_controller_feedback)
    proto_agent_update = test_agent_update_protogen_creator()
    print (proto_agent_update)


if __name__ == "__main__":
    main()