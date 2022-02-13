import re


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


if __name__ == "__main__":
    input_file = "input/day_14.txt"

    part_one_res = part_one(input_file)
    print(f"{part_one_res=}")
