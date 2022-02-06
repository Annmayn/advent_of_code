from pydantic import BaseModel

Direction = tuple[str, int]


def read_input(input_file: str) -> list[Direction]:
    dir_arr: list[Direction] = []
    with open(input_file, "r") as f:
        for each in f:
            dir = each[0]
            path = int(each[1:])
            dir_arr.append((dir, path))
    return dir_arr


def part_one(data: list[Direction]) -> int:
    curr_dir = "E"
    dir_map = {"E": ("N", "S"), "N": ("W", "E"), "W": ("S", "N"), "S": ("E", "W")}
    manhattan_distance = [0, 0]
    for dir, val in data:
        if dir in ("W", "S"):
            val *= -1
        if dir in ("E", "W"):
            manhattan_distance[0] += val
        elif dir in ("N", "S"):
            manhattan_distance[1] += val
        elif dir == "F":
            if curr_dir in ("W", "S"):
                val *= -1
            if curr_dir in ("E", "W"):
                manhattan_distance[0] += val
            if curr_dir in ("N", "S"):
                manhattan_distance[1] += val
        elif dir == "L":
            val %= 360
            while val > 0:
                curr_dir = dir_map[curr_dir][0]
                val -= 90
        elif dir == "R":
            val %= 360
            while val > 0:
                curr_dir = dir_map[curr_dir][1]
                val -= 90
    return abs(manhattan_distance[0]) + abs(manhattan_distance[1])

def part_two(data: list[Direction]) -> int:
    waypoint_pos = [10, 1]
    dir_map = {"E": ("N", "S"), "N": ("W", "E"), "W": ("S", "N"), "S": ("E", "W")}
    manhattan_distance = [0, 0]
    for dir, val in data:
        if dir in ("W", "S"):
            val *= -1
        if dir in ("E", "W"):
            waypoint_pos[0] += val
        elif dir in ("N", "S"):
            waypoint_pos[1] += val
        elif dir == "F":
            manhattan_distance[0] += waypoint_pos[0] * val
            manhattan_distance[1] += waypoint_pos[1] * val
        elif dir == "L":
            val %= 360
            d1, d2 = 'E', 'N'
            while val > 0:
                d1 = dir_map[d1][0]
                d2 = dir_map[d1][0]
                val -= 90
            val_1, val_2 = 0, 0
            if d1 == 'W':
                val_1 = -waypoint_pos[0]
            elif d1 == 'N':
                val_2 = waypoint_pos[0]
            elif d1 == 'S':
                val_2 = -waypoint_pos[0]

            if d2 == 'S':
                val_2 = -waypoint_pos[1]
            elif d2 == 'E':
                val_1 = waypoint_pos[1]
            elif d2 == 'W':
                val_1 = -waypoint_pos[1]

            waypoint_pos = [val_1, val_2]
        elif dir == "R":
            val %= 360
            d1, d2 = 'E', 'N'
            while val > 0:
                d1 = dir_map[d1][1]
                d2 = dir_map[d2][1]
                val -= 90
            val_1, val_2 = 0, 0
            if d1 == 'W':
                val_1 = -waypoint_pos[0]
            elif d1 == 'N':
                val_2 = waypoint_pos[0]
            elif d1 == 'S':
                val_2 = -waypoint_pos[0]
            if d2 == 'E':
                val_1 = waypoint_pos[1]
            elif d2 == 'W':
                val_1 = -waypoint_pos[1]
            elif d2 == 'S':
                val_2 = -waypoint_pos[1]

            waypoint_pos = [val_1, val_2]
    return abs(manhattan_distance[0]) + abs(manhattan_distance[1])

if __name__ == "__main__":
    input_file = "input/day_12.txt"
    data: list[Direction] = read_input(input_file)

    part_one_res = part_one(data)
    print(f"{part_one_res=}")

    part_two_res = part_two(data)
    print(f"{part_two_res=}")
