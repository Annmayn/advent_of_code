def part_one(inp_file: str):
    counter = 0
    with open(inp_file, "r") as f:
        for inp in f:
            if is_valid_one(inp):
                counter += 1
    return counter

def part_two(inp_file: str):
    counter = 0
    with open(inp_file, "r") as f:
        for inp in f:
            if is_valid_two(inp):
                counter += 1
    return counter


def is_valid_one(inp: str) -> bool:
    (check_range, check_val, pwd) = inp.split()
    (lower_bound, upper_bound) = map(int, check_range.split("-"))
    check_val = check_val.removesuffix(":")
    count = pwd.count(check_val)
    return lower_bound <= count <= upper_bound

def is_valid_two(inp: str) -> bool:
    (check_range, check_val, pwd) = inp.split()
    (lower_ind, upper_ind) = map(int, check_range.split("-"))
    check_val = check_val.removesuffix(":")
    is_exist_one = pwd[lower_ind-1] == check_val
    is_exist_two = pwd[upper_ind - 1] == check_val

    return is_exist_one ^ is_exist_two


if __name__ == "__main__":
    inp_file = "input/day_2.txt"

    count_part_one = part_one(inp_file)
    print(f"{count_part_one=}")

    count_part_two = part_two(inp_file)
    print(f"{count_part_two=}")
