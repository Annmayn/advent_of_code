from copy import deepcopy
from pydantic import BaseModel


class Direction(BaseModel):
    dirn: str
    val: int


class Position:
    def __init__(self, east_pos: int = 0, north_pos: int = 0):
        self.east_pos: int = east_pos
        self.north_pos: int = north_pos

    def __repr__(self):
        return f"east: {self.east_pos} | north: {self.north_pos}"

    def manhattan_distance(self) -> int:
        return abs(self.east_pos) + abs(self.north_pos)


DIR_MAP = {"E": ("N", "S"), "N": ("W", "E"), "W": ("S", "N"), "S": ("E", "W")}


def read_input(input_file: str) -> list[Direction]:
    dir_arr: list[Direction] = []
    with open(input_file, "r") as f:
        for each in f:
            dir = each[0]
            path = int(each[1:])
            dir_arr.append(Direction(dirn=dir, val=path))
    return dir_arr


def part_one(data: list[Direction]) -> int:
    curr_dir = "E"
    pos = Position()
    for each in data:
        dir = curr_dir if each.dirn == "F" else each.dirn

        if dir in ("W", "S"):
            each.val *= -1

        if dir in ("E", "W"):
            pos.east_pos += each.val
        elif dir in ("N", "S"):
            pos.north_pos += each.val
        elif dir in ("L", "R"):
            ind = 0 if dir == "L" else 1
            each.val %= 360
            while each.val > 0:
                curr_dir = DIR_MAP[curr_dir][ind]
                each.val -= 90
    return pos.manhattan_distance()


def part_two(data: list[Direction]) -> int:
    waypoint = Position(10, 1)
    ship = Position()
    for each in data:
        if each.dirn in ("W", "S"):
            each.val *= -1

        if each.dirn in ("E", "W"):
            waypoint.east_pos += each.val
        elif each.dirn in ("N", "S"):
            waypoint.north_pos += each.val
        elif each.dirn == "F":
            ship.east_pos += waypoint.east_pos * each.val
            ship.north_pos += waypoint.north_pos * each.val
        elif each.dirn in ("L", "R"):
            ind = 0 if each.dirn == "L" else 1
            each.val %= 360
            d1, d2 = "E", "N"
            while each.val > 0:
                d1 = DIR_MAP[d1][ind]
                d2 = DIR_MAP[d2][ind]
                each.val -= 90

            east_pos = (
                -waypoint.east_pos
                if d1 == "W"
                else waypoint.north_pos
                if d2 == "E"
                else -waypoint.north_pos
                if d2 == "W"
                else waypoint.east_pos
            )
            north_pos = (
                waypoint.east_pos
                if d1 == "N"
                else -waypoint.east_pos
                if d1 == "S"
                else -waypoint.north_pos
                if d2 == "S"
                else waypoint.north_pos
            )

            waypoint.east_pos = east_pos
            waypoint.north_pos = north_pos
    return ship.manhattan_distance()


if __name__ == "__main__":
    input_file = "input/day_12.txt"
    data: list[Direction] = read_input(input_file)

    data_copy = deepcopy(data)
    part_one_res = part_one(data_copy)
    print(f"{part_one_res=}")

    data_copy = deepcopy(data)
    part_two_res = part_two(data)
    print(f"{part_two_res=}")
