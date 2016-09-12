from enum import Enum


class Position(Enum):
    point_guard = "point guard"
    shooting_guard = "shooting guard"
    small_forward = "small forward"
    power_forward = "power forward"
    guard = "guard"
    forward = "forward"
    center = "center"
    guard_forward = "guard-forward"
    forward_guard = "forward-guard"
    forward_center = "forward-center"
    unknown = ""

    @staticmethod
    def from_name(name):
        position = position_name_map.get(name.lower())

        if position is None:
            raise ValueError("Unknown position name: %s", name)

        return position

    @staticmethod
    def from_abbreviation(abbreviation):
        position = position_abbreviation_map.get(abbreviation.lower())

        if position is None:
            raise ValueError("Unknown position abbreviation")

        return position


position_name_map = {
    "point guard": Position.point_guard,
    "shooting guard": Position.shooting_guard,
    "small forward": Position.small_forward,
    "power forward": Position.power_forward,
    "center": Position.center,
    "guard": Position.guard,
    "forward": Position.forward,
    "guard-forward": Position.guard_forward,
    "forward-guard": Position.forward_guard,
    "forward-center": Position.forward_center,
    "": Position.unknown,
}

position_abbreviation_map = {
    "PG": Position.point_guard,
    "SG": Position.shooting_guard,
    "SF": Position.small_forward,
    "PF": Position.power_forward,
    "C": Position.center,
    "G": Position.guard,
    "F": Position.forward,
    "GF": Position.guard_forward,
    "FG": Position.forward_guard,
    "FC": Position.forward_center,
    "": Position.unknown,
}
