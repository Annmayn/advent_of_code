from ast import Call
from typing import Callable, Optional


Data = list[str]
Function = Callable[[int, int], int]

func_map: dict[str, Function] = {"+": lambda x, y: x + y, "*": lambda x, y: x * y}


def read_input(input_file: str) -> Data:
    data: Data = []
    with open(input_file, "r") as f:
        for row in f:
            data.append(row.replace(" ", ""))
    return data


def part_one(data: Data) -> int:
    total_sum = 0
    for expression in data:
        res, _ = solve(expression, ind=0)
        total_sum += res
    return total_sum


def solve(
    expr: str,
    ind: int,
    res: int = 0,
    prev_data: int = 0,
    func_name: str = "+",
) -> tuple[int, int]:
    if ind >= len(expr):
        return res, ind
    while ind < len(expr):
        data = expr[ind]
        if data == "(":
            curr_data, new_ind = solve(expr, ind + 1)
            ind = new_ind
        elif expr[ind - 1] == ")":
            return res, ind - 1
        else:
            curr_data = int(data)
        func = func_map.get(func_name)
        if func is None:
            return res, ind
        res = func(prev_data, curr_data)
        prev_data = res
        ind += 1
        func_name = expr[ind] if ind < len(expr) else ""
        ind += 1
    return res, ind


if __name__ == "__main__":
    input_file = "input/day_18.txt"
    data = read_input(input_file)
    part_one_res = part_one(data)
    print(f"{part_one_res=}")
