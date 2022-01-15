import re
from typing import Callable, Iterable


def part_one(input_file: str) -> int:
    num_valid_passport = 0
    for batch_input in get_batch_input(input_file):
        if is_valid_part_one(batch_input):
            num_valid_passport += 1
    return num_valid_passport


def part_two(input_file: str) -> int:
    num_valid_passport = 0
    for batch_input in get_batch_input(input_file):
        if is_valid_part_two(batch_input):
            num_valid_passport += 1
    return num_valid_passport


def get_batch_input(input_file: str) -> Iterable[str]:
    with open(input_file, "r") as f:
        res = []
        while True:
            try:
                next_res = next(f).strip()
                if next_res:
                    res.append(next_res)
                else:
                    yield " ".join(res)
                    res = []
            except StopIteration:
                if res:
                    yield " ".join(res)
                break


def is_valid_part_one(batch_input: str) -> bool:
    valid_checklist = {
        "byr": False,
        "iyr": False,
        "eyr": False,
        "hgt": False,
        "hcl": False,
        "ecl": False,
        "pid": False,
        "cid": True,
    }
    key_value_list: list[str] = batch_input.split()
    for key_value in key_value_list:
        key, _ = key_value.split(":")
        valid_checklist[key] = True
    return all(valid_checklist.values())


def is_valid_part_two(batch_input: str) -> bool:
    def is_valid_height(height: str):
        if height.endswith("cm"):
            height = height.removesuffix("cm")
            return 150 <= int(height) <= 193
        elif height.endswith("in"):
            height = height.removesuffix("in")
            return 59 <= int(height) <= 76
        return False

    valid_checklist = {
        "byr": False,
        "iyr": False,
        "eyr": False,
        "hgt": False,
        "hcl": False,
        "ecl": False,
        "pid": False,
        "cid": True,
    }
    validator_map: dict[str, Callable[[str], bool]] = {
        "byr": lambda x: 1920 <= int(x) <= 2002,
        "iyr": lambda x: 2010 <= int(x) <= 2020,
        "eyr": lambda x: 2020 <= int(x) <= 2030,
        "hgt": lambda x: is_valid_height(x),
        "hcl": lambda x: re.match(r"^#[0-9a-f]{6}$", x) is not None,
        "ecl": lambda x: x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
        "pid": lambda x: re.match(r"^[0-9]{9}$", x) is not None,
        "cid": lambda x: True,
    }
    key_value_list: list[str] = batch_input.split()
    for key_value in key_value_list:
        key, value = key_value.split(":")
        validator_func = validator_map[key]
        if validator_func(value):
            valid_checklist[key] = True
    return all(valid_checklist.values())


if __name__ == "__main__":
    input_file = "input/day_4.txt"
    part_one_valid_passports = part_one(input_file)
    print(f"{part_one_valid_passports=}")

    part_two_valid_passports = part_two(input_file)
    print(f"{part_two_valid_passports=}")
