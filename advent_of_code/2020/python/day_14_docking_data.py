import re
import typing


def part_one(input_file: str) -> int:
    memory: dict[str, int] = {}
    mask: str = ""
    mem_pattern = r"mem\[(?P<addr>\d+)\]\s+=\s+(?P<value>\d+)"
    with open(input_file, "r") as f:
        for row in f:
            if row.startswith("mask"):
                mask = row.split()[-1]

            elif row.startswith("mem"):
                res = re.match(mem_pattern, row)
                if res is None:
                    continue
                mem_info = res.groupdict()
                memory[mem_info["addr"]] = int(
                    add_mask(int(mem_info["value"]), mask), 2
                )
    return sum(memory.values())


def add_mask(inp: int, mask: str) -> str:
    inp_bin = f"{inp:036b}"
    return "".join([j if j != "X" else i for i, j in zip(inp_bin, mask)])


def part_two(input_file: str) -> int:
    memory: dict[str, int] = {}
    mask: str = ""
    mem_pattern = r"mem\[(?P<addr>\d+)\]\s+=\s+(?P<value>\d+)"
    with open(input_file, "r") as f:
        for row in f:
            if row.startswith("mask"):
                mask = row.split()[-1]

            elif row.startswith("mem"):
                res = re.match(mem_pattern, row)
                if res is None:
                    continue
                mem_info = res.groupdict()
                for mem_addr in valid_mem_addr(int(mem_info["addr"]), mask):
                    memory[mem_addr] = int(mem_info["value"])
    return sum(memory.values())


def valid_mem_addr(inp: int, mask: str) -> typing.Iterator[str]:
    inp_bin = f"{inp:036b}"

    masked_inp = [j if j in ("X", "1") else i for i, j in zip(inp_bin, mask)]
    n = 2 ** masked_inp.count("X")
    for i in range(n):
        sup_x = list(f"{i:036b}")
        new_inp = substitute(masked_inp.copy(), sup_x)
        yield new_inp


def substitute(inp: list[str], sup: list[str]) -> str:
    for i, val in enumerate(inp):
        if val == "X":
            inp[i] = sup.pop()
    return "".join(inp)


if __name__ == "__main__":
    input_file = "input/day_14.txt"

    part_one_res = part_one(input_file)
    print(f"{part_one_res=}")

    part_two_res = part_two(input_file)
    print(f"{part_two_res=}")
