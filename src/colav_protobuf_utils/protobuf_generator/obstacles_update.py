from colav_protobuf import ObstaclesUpdate
from typing import List


@staticmethod
def gen_protobuf_obstacles_update(
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
            obstacles_update.dynamic_obstacles[idx] = obstacle

        for idx, obstacle in enumerate(static_obstacles):
            obstacles_update.static_obstacles.add()
            obstacles_update.static_obstacles[idx] = obstacle

        obstacles_update.timestamp = timestamp
    except Exception as e:
        raise Exception(e)

    return obstacles_update
