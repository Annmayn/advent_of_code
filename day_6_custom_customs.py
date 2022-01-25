from typing import Optional


def part_one(input_file: str) -> int:
    counter = 0
    unique_ans: set[str] = set()
    with open(input_file, "r") as f:
        for row in f:
            if row.strip() == "":
                counter += len(unique_ans)
                unique_ans = set()
            else:
                for val in row.strip():
                    unique_ans.add(val)
        if unique_ans:
            counter += len(unique_ans)
    return counter


def part_two(input_file: str) -> int:
    counter = 0
    unique_ans: Optional[set[str]] = None
    with open(input_file, "r") as f:
        for row in f:
            if row.strip() == "":
                counter += len(unique_ans) if unique_ans is not None else 0
                unique_ans = None
            else:
                row_set: set[str] = {val for val in row.strip()}
                unique_ans = (
                    unique_ans.intersection(row_set)
                    if unique_ans is not None
                    else row_set
                )
        if unique_ans:
            counter += len(unique_ans)
    return counter


if __name__ == "__main__":
    input_file = "input/day_6.txt"
    part_one_res = part_one(input_file)
    print(f"{part_one_res=}")

    part_two_res = part_two(input_file)
    print(f"{part_two_res=}")
