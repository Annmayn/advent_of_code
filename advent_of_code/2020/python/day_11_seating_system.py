from copy import deepcopy
from typing import Iterator

DataList = list[list[str]]


def read_input(input_file: str) -> DataList:
    with open(input_file, "r") as f:
        data = f.read()
    data_arr = [list(row) for row in data.strip().split("\n")]
    return data_arr


def part_one(data: DataList) -> int:
    prev_data = None
    while prev_data is None or prev_data != data:
        counter = 0
        prev_data = deepcopy(data)
        for i, row in enumerate(data):
            for j, val in enumerate(row):
                occupied_count = get_occupied_count((i, j), prev_data)
                if val == "L" and occupied_count == 0:
                    data[i][j] = "#"
                elif val == "#" and occupied_count >= 4:
                    data[i][j] = "L"
                if data[i][j] == "#":
                    counter += 1
    return counter


def get_occupied_count(pos: tuple[int, int], data: DataList) -> int:
    (x, y) = pos
    max_row = len(data)
    max_col = len(data[0])
    counter = 0
    for i, j in get_neighbors(x, y):
        if is_valid((i, j), max_row, max_col) and data[i][j] == "#":
            counter += 1
    return counter


def get_neighbors(x: int, y: int) -> Iterator[tuple[int, int]]:
    neighbors = [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x + 1, y),
        (x + 1, y + 1),
        (x, y + 1),
        (x - 1, y + 1),
        (x - 1, y),
    ]
    for neigh in neighbors:
        yield neigh


def is_valid(pos: tuple[int, int], max_row: int, max_col: int) -> bool:
    x, y = pos
    return x >= 0 and x < max_row and y >= 0 and y < max_col


def part_two(data: DataList) -> int:
    prev_data = None
    iter = 1
    while prev_data is None or prev_data != data:
        iter += 1
        counter = 0
        prev_data = deepcopy(data)
        for i, row in enumerate(data):
            for j, val in enumerate(row):
                occupied_count = get_elongated_occupied_count((i, j), prev_data)
                if val == "L" and occupied_count == 0:
                    data[i][j] = "#"
                elif val == "#" and occupied_count >= 5:
                    data[i][j] = "L"
                if data[i][j] == "#":
                    counter += 1
    return counter


def get_elongated_occupied_count(pos: tuple[int, int], data: DataList) -> int:
    (x, y) = pos
    max_row = len(data)
    max_col = len(data[0])
    counter = 0
    for (i, j), val in get_elongated_neighbors(x, y, data):
        if val == "#":
            counter += 1
    return counter


def get_elongated_neighbors(
    x: int, y: int, data: DataList
) -> Iterator[tuple[tuple[int, int], str]]:
    max_row = len(data)
    max_col = len(data[0])
    VALID_VAL = ("#", "L")

    attrs = [
        (0, 1, max_row, max_col),
        (1, 1, max_row, max_col),
        (1, 0, max_row, max_col),
        (1, -1, max_row, -1),
        (0, -1, max_row, -1),
        (-1, -1, -1, -1),
        (-1, 0, -1, max_col),
        (-1, 1, -1, max_col),
    ]
    for i, j, row_boundary, col_boundary in attrs:
        row = x + i
        col = y + j
        while row != row_boundary and col != col_boundary:
            if data[row][col] in VALID_VAL:
                yield ((row, col), data[row][col])
                break
            row += i
            col += j


if __name__ == "__main__":
    input_file = "input/day_11.txt"
    data = read_input(input_file)

    data_copy = deepcopy(data)
    part_one_res = part_one(data_copy)
    print(f"{part_one_res=}")

    data_copy = deepcopy(data)
    part_two_res = part_two(data_copy)
    print(f"{part_two_res=}")
