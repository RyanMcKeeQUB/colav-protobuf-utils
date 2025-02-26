from colav_protobuf_utils.protobuf_generator import gen_mission_request, VesselType
from colav_protobuf_utils.protobuf_generator import (
    gen_controller_feedback,
    CTRLStatus,
    CTRLMode,
)
from colav_protobuf_utils.protobuf_generator import gen_agent_update
from colav_protobuf_utils.protobuf_generator import (
    gen_obstacles_update,
    gen_static_obstacle,
    gen_dynamic_obstacle,
    StaticObstacleTypeEnum,
    DynamicObstacleTypeEnum,
)
from colav_protobuf_utils.protobuf_generator import (
    gen_mission_response,
    MissionResponseTypeEnum,
)
from colav_protobuf_utils.serialization import serialise_protobuf
from colav_protobuf_utils.deserialization import deserialise_protobuf

# from colav_protobuf_utils.deserialization import deserialize_protobuf_message


def test_mission_request_protogen_creator():
    return gen_mission_request(
        tag="MOCK_MISSION",
        timestamp="000002000301",
        vessel_tag="MOCK_AGENTS",
        vessel_type=VesselType.HYDROFOIL,
        vessel_max_acceleration=float(5.0),
        vessel_max_deceleration=float(2.0),
        vessel_max_velocity=float(30),
        vessel_min_velocity=float(15.0),
        vessel_max_yaw_rate=float(0.2),
        vessel_loa=float(2.0),
        vessel_beam=float(0.5),
        vessel_safety_radius=float(2.0),
        cartesian_init_position=[float(1), float(1), float(2)],
        cartesian_goal_position=[float(1), float(1), float(5)],
        goal_safety_radius=float(15),
    )


def test_mission_response_protogen_creator():
    return gen_mission_response(
        tag="MOCK_MISSION",
        timestamp="000012300",
        response_type=MissionResponseTypeEnum.MISSION_STARTING,
        response_details="Mission accepted",
    )


def test_agent_update_protogen_creator():
    return gen_agent_update(
        mission_tag="MOCK_MISSION",
        agent_tag="MOCK_AGENT",
        cartesian_position=[0, 0, 0],
        quaternium_orientation=[0, 0, 0, 1],
        velocity=15,
        yaw_rate=0.2,
        acceleration=0.2,
        timestamp="000012300",
    )


def test_dynamic_obstacle_protogen_creator():
    return [
        gen_dynamic_obstacle(
            tag="MOCK_DYNAMIC_OBSTACLE",
            type=DynamicObstacleTypeEnum.VESSEL,
            cartesian_position=[10, 3, 2],
            quaternium_orientation=[0, 0, 0, 1],
            velocity=15,
            yaw_rate=0.2,
            loa=2,
            beam=0.5,
            safety_radius=2,
        )
    ]


def test_static_obstacle_protogen_creator():
    return [
        gen_static_obstacle(
            tag="MOCK_STATIC_OBSTACLE",
            type=StaticObstacleTypeEnum.BUOY,
            cartesian_position=[10, 3, 2],
            quaternium_orientation=[0, 0, 0, 1],
            polyshape_points=[(0, 0, 0), (0, 0, 0), (0, 0, 0)],
            inflation_radius=2,
        )
    ]


def test_obstacles_update_protogen_creator():
    dynamic_obstacle_list = test_dynamic_obstacle_protogen_creator()
    static_obstacle_list = test_static_obstacle_protogen_creator()

    return gen_obstacles_update(
        mission_tag="MOCK_MISSION",
        dynamic_obstacles=dynamic_obstacle_list,
        static_obstacles=static_obstacle_list,
        timestamp="000012300",
    )


def test_controller_feedback_protogen_creator():
    return gen_controller_feedback(
        mission_tag="MOCK MISSION",
        agent_tag="mock agent",
        ctrl_mode=CTRLMode.CRUISE,
        ctrl_status=CTRLStatus.ACTIVE,
        velocity=float(15),
        yaw_rate=float(0.2),
        timestamp="0000012304",
    )


def main():
    proto_mission_request = test_mission_request_protogen_creator()
    print(proto_mission_request)

    proto_mission_response = test_mission_response_protogen_creator()
    print(proto_mission_response)

    proto_agent_update = test_agent_update_protogen_creator()
    print(proto_agent_update)

    proto_obstacles_update = test_obstacles_update_protogen_creator()
    print(proto_obstacles_update)
    serialised_obstacles_update = serialise_protobuf(proto_obstacles_update)
    deserialised_obstacles_update = deserialise_protobuf(serialised_obstacles_update)
    print(deserialised_obstacles_update, type="mission_request")
    proto_controller_feedback = test_controller_feedback_protogen_creator()
    print(proto_controller_feedback)


if __name__ == "__main__":
    main()
