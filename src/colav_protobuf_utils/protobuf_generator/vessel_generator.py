from enum import Enum


class VesselType(Enum):
    UNSPECIFIED = 0
    HYDROFOIL = 1
    OTHER = 2


def gen_vessel(
    tag: str,
    type: VesselType,
    max_acceleration: float,
    max_deceleration: float,
    max_velocity: float,
    min_velocity: float,
    max_yaw_rate: float,
    loa: float,  # Length Overall
    beam: float,  # breadth
    safety_radius: float,
):
    pass
