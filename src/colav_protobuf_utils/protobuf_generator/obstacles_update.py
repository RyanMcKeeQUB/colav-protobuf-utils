from colav_protobuf import ObstaclesUpdate
from typing import List, Tuple
from enum import Enum


class DynamicObstacleTypeEnum(Enum):
    UNSPECIFIED = ObstaclesUpdate.DynamicObstacleType.DYNAMIC_UNSPECIFIED
    VESSEL = ObstaclesUpdate.DynamicObstacleType.VESSEL


class StaticObstacleTypeEnum(Enum):
    STATIC_UNSPECIFIED = ObstaclesUpdate.StaticObstacleType.STATIC_UNSPECIFIED
    BUOY = ObstaclesUpdate.StaticObstacleType.BUOY
    LAND_MASS = ObstaclesUpdate.StaticObstacleType.LAND_MASS


def gen_dynamic_obstacle(
    tag: str,
    type: DynamicObstacleTypeEnum,
    cartesian_position: Tuple[float, float, float],
    quaternium_orientation: Tuple[float, float, float, float],
    loa: float,
    beam: float,
    safety_radius: float,
    velocity: float,
    yaw_rate: float,
) -> ObstaclesUpdate.DynamicObstacle:
    try:
        dynamic_obstacle = ObstaclesUpdate.DynamicObstacle()
        dynamic_obstacle.tag = tag
        dynamic_obstacle.type = type.value
        dynamic_obstacle.state.pose.position.x = cartesian_position[0]
        dynamic_obstacle.state.pose.position.y = cartesian_position[1]
        dynamic_obstacle.state.pose.position.z = cartesian_position[2]

        dynamic_obstacle.state.pose.orientation.x = quaternium_orientation[0]
        dynamic_obstacle.state.pose.orientation.y = quaternium_orientation[1]
        dynamic_obstacle.state.pose.orientation.z = quaternium_orientation[2]
        dynamic_obstacle.state.pose.orientation.w = quaternium_orientation[3]

        dynamic_obstacle.state.velocity = velocity
        dynamic_obstacle.state.yaw_rate = yaw_rate

        dynamic_obstacle.geometry.loa = loa
        dynamic_obstacle.geometry.beam = beam
        dynamic_obstacle.geometry.safety_radius = safety_radius
    except Exception as e:
        raise e

    return dynamic_obstacle


def gen_static_obstacle(
    tag: str,
    type: StaticObstacleTypeEnum,
    cartesian_position: Tuple[float, float, float],
    quaternium_orientation: Tuple[float, float, float, float],
    polyshape_points: List[Tuple[float, float, float]],
    inflation_radius: float,
) -> ObstaclesUpdate.StaticObstacle:
    try:
        static_obstacle = ObstaclesUpdate.StaticObstacle()
        static_obstacle.tag = tag
        static_obstacle.type = type.value
        static_obstacle.pose.position.x = cartesian_position[0]
        static_obstacle.pose.position.y = cartesian_position[1]
        static_obstacle.pose.position.z = cartesian_position[2]

        static_obstacle.pose.orientation.x = quaternium_orientation[0]
        static_obstacle.pose.orientation.y = quaternium_orientation[1]
        static_obstacle.pose.orientation.z = quaternium_orientation[2]
        static_obstacle.pose.orientation.w = quaternium_orientation[3]

        static_obstacle.geometry.inflation_radius = inflation_radius
        for point in polyshape_points:
            static_obstacle.geometry.polyshape_points.add()
            static_obstacle.geometry.polyshape_points[-1].x = point[0]
            static_obstacle.geometry.polyshape_points[-1].y = point[1]
            static_obstacle.geometry.polyshape_points[-1].z = point[2]
    except Exception as e:
        raise e

    return static_obstacle


def gen_obstacles_update(
    mission_tag: str,
    dynamic_obstacles: List[ObstaclesUpdate.DynamicObstacle],
    static_obstacles: List[ObstaclesUpdate.StaticObstacle],
    timestamp: str,
) -> ObstaclesUpdate:
    """Generates a protobuf message for obstacles update"""
    try:
        obstacles_update = ObstaclesUpdate()
        obstacles_update.mission_tag = mission_tag
        # need to do the repeated thing

        for idx, obstacle in enumerate(dynamic_obstacles):
            obstacles_update.dynamic_obstacles.add()
            obstacles_update.dynamic_obstacles[idx].tag = obstacle.tag
            obstacles_update.dynamic_obstacles[idx].type = obstacle.type
            obstacles_update.dynamic_obstacles[idx].state.pose.position.x = (
                obstacle.state.pose.position.x
            )
            obstacles_update.dynamic_obstacles[idx].state.pose.position.y = (
                obstacle.state.pose.position.y
            )
            obstacles_update.dynamic_obstacles[idx].state.pose.position.z = (
                obstacle.state.pose.position.z
            )
            obstacles_update.dynamic_obstacles[idx].state.pose.orientation.x = (
                obstacle.state.pose.orientation.x
            )
            obstacles_update.dynamic_obstacles[idx].state.pose.orientation.y = (
                obstacle.state.pose.orientation.y
            )
            obstacles_update.dynamic_obstacles[idx].state.pose.orientation.z = (
                obstacle.state.pose.orientation.z
            )
            obstacles_update.dynamic_obstacles[idx].state.pose.orientation.w = (
                obstacle.state.pose.orientation.w
            )
            obstacles_update.dynamic_obstacles[idx].state.velocity = (
                obstacle.state.velocity
            )
            obstacles_update.dynamic_obstacles[idx].state.yaw_rate = (
                obstacle.state.yaw_rate
            )
            obstacles_update.dynamic_obstacles[idx].geometry.loa = obstacle.geometry.loa
            obstacles_update.dynamic_obstacles[idx].geometry.beam = (
                obstacle.geometry.beam
            )
            obstacles_update.dynamic_obstacles[idx].geometry.safety_radius = (
                obstacle.geometry.safety_radius
            )

        for idx, obstacle in enumerate(static_obstacles):
            obstacles_update.static_obstacles.add()
            obstacles_update.static_obstacles[idx].tag = obstacle.tag
            obstacles_update.static_obstacles[idx].type = obstacle.type
            obstacles_update.static_obstacles[idx].pose.position.x = (
                obstacle.pose.position.x
            )
            obstacles_update.static_obstacles[idx].pose.position.y = (
                obstacle.pose.position.y
            )
            obstacles_update.static_obstacles[idx].pose.position.z = (
                obstacle.pose.position.z
            )
            obstacles_update.static_obstacles[idx].pose.orientation.x = (
                obstacle.pose.orientation.x
            )
            obstacles_update.static_obstacles[idx].pose.orientation.y = (
                obstacle.pose.orientation.y
            )
            obstacles_update.static_obstacles[idx].pose.orientation.z = (
                obstacle.pose.orientation.z
            )
            obstacles_update.static_obstacles[idx].pose.orientation.w = (
                obstacle.pose.orientation.w
            )
            obstacles_update.static_obstacles[idx].geometry.inflation_radius = (
                obstacle.geometry.inflation_radius
            )
            for point in obstacle.geometry.polyshape_points:
                obstacles_update.static_obstacles[idx].geometry.polyshape_points.add()
                obstacles_update.static_obstacles[idx].geometry.polyshape_points[
                    -1
                ].x = point.x
                obstacles_update.static_obstacles[idx].geometry.polyshape_points[
                    -1
                ].y = point.y
                obstacles_update.static_obstacles[idx].geometry.polyshape_points[
                    -1
                ].z = point.z

        obstacles_update.timestamp = timestamp
    except Exception as e:
        raise e

    return obstacles_update
