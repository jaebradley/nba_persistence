from enum import Enum

from nba_data.data.position import Position as NbaDataPosition


class Position(Enum):
    point_guard = "point guard"
    shooting_guard = "shooting guard"
    small_forward = "small forward"
    power_forward = "power forward"
    guard = NbaDataPosition.guard.value
    forward = NbaDataPosition.forward.value
    center = NbaDataPosition.center.value
