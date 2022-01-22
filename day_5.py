import math


def part_one(input_file):
    max_id = 0
    with open(input_file, "r") as f:
        for each in f:
            id, _, _ = find_id(each)
            if id > max_id:
                max_id = id
    print(f"{max_id=}")


def part_two(input_file):
    unvisited_pos = {(i, j) for i in range(128) for j in range(8)}
    id = -1
    with open(input_file, "r") as f:
        for each in f:
            _, row, col = find_id(each)
            unvisited_pos.remove((row, col))
        ids = []
        for pos in unvisited_pos:
            # if both neighboring ids not in unvisited list
            # must mean they're valid ticket ids that we've scanned
            if (
                reduce_by_one(pos) not in unvisited_pos
                and increase_by_one(pos) not in unvisited_pos
            ):
                id = pos[0] * 8 + pos[1]
                break
    print(f"{id=}")


def reduce_by_one(pos) -> tuple[int, int]:
    r, c = pos
    c -= 1
    if c < 0:
        c = 7
        r -= 1
    return (r, c)


def increase_by_one(pos) -> tuple[int, int]:
    r, c = pos
    c += 1
    if c > 7:
        c = 0
        r += 1
    return (r, c)


def find_id(ticket: str) -> tuple[int, int, int]:
    row_info = ticket[:7]
    col_info = ticket[7:]
    row = find_row(row_info)
    col = find_col(col_info)
    return row * 8 + col, row, col


def find_row(row_info: str, range=(0, 127)) -> int:
    mid_val = 0
    for current in row_info:
        mid_val = range[0] + (range[1] - range[0]) / 2
        if current == "F":
            mid_val = math.floor(mid_val)
            range = (range[0], mid_val)
        elif current == "B":
            mid_val = math.ceil(mid_val)
            range = (mid_val, range[1])
    return mid_val


def find_col(col_info: str, range=(0, 7)) -> int:
    mid_val = 0
    for current in col_info:
        mid_val = range[0] + (range[1] - range[0]) / 2
        if current == "L":
            mid_val = math.floor(mid_val)
            range = (range[0], mid_val)
        elif current == "R":
            mid_val = math.ceil(mid_val)
            range = (mid_val, range[1])
    return mid_val


if __name__ == "__main__":
    input_file = "input/day_5.txt"
    part_one(input_file)
    part_two(input_file)
    # res = find_id("BBFFBBFRLL")
    # print(f"{res=}")
