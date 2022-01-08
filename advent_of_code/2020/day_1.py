#!/usr/bin/python
from typing import Set, Optional


def two_sum(inp: Set[int], total_sum: int) -> Optional[int]:
    """
    doesn't work if entry can be repeated as `inp` is a set
    """
    for val in inp:
        other_val = total_sum - val
        if val != other_val and other_val in inp:
            return val * other_val
    return None


def three_sum(inp: set[int], total_sum: int) -> Optional[int]:
    """
    doesn't work if entry can be repeated
    edge case:
        might use the same number twice
        eg:
        total_sum = 11
        inp = [2, 3, 4, 6]
        expected = 2 * 3 * 6
        function might return either (3 * 4 * 4) or (2 * 3 * 6)
        depending on the first observed value
    """
    for val in inp:
        new_inp = inp.copy()
        new_inp.remove(val)
        res = two_sum(inp, total_sum - val)
        if res:
            return val * res
    return None


if __name__ == "__main__":
    input_file = "input/day_1.txt"
    with open(input_file, "r") as f:
        inp = f.readlines()
    inp_parsed = {int(each) for each in inp}
    total_sum = 2020

    two_sum_res = two_sum(inp_parsed, total_sum)
    print(f"{two_sum_res=}")

    three_sum_res = three_sum(inp_parsed, total_sum)
    print(f"{three_sum_res=}")
