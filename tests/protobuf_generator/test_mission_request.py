# from colav_protobuf_utils.protobuf_generator import gen_mission_request
# from colav_protobuf.examples import mission_request
# import pytest


# def test_gen_mission_request():
#     proto_utils_mission_request = gen_mission_request(
#         tag=mission_request.tag,
#         timestamp=mission_request.timestamp,
#         vessel_tag=mission_request.vessel.tag,
#         vessel_type=mission_request.vessel.type,
#         vessel_max_acceleration=mission_request.vessel.constraints.max_acceleration,
#         vessel_max_deceleration=mission_request.vessel.constraints.max_deceleration,
#         vessel_max_velocity=mission_request.vessel.constraints.max_velocity,
#         vessel_min_velocity=mission_request.vessel.constraints.min_velocity,
#         vessel_max_yaw_rate=mission_request.vessel.constraints.max_yaw_rate,
#         vessel_loa=mission_request.vessel.geometry.loa,
#         vessel_beam=mission_request.vessel.geometry.beam,
#         vessel_safety_radius=mission_request.vessel.geometry.safety_radius,
#         cartesian_init_position=(
#             mission_request.init_position.x,
#             mission_request.init_position.y,
#             mission_request.init_position.z,
#         ),
#         cartesian_goal_position=(
#             mission_request.goal_waypoint.position.x,
#             mission_request.goal_waypoint.position.y,
#             mission_request.goal_waypoint.position.z,
#         ),
#         goal_safety_radius=mission_request.goal_waypoint.safety_radius,
#     )
#     # assert proto_utils_mission_request.tag == mission_request.tag
#     # assert proto_utils_mission_request.timestamp == mission_request.timestamp
