import math


def read_input(input_file: str) -> tuple[int, list[str]]:
    with open(input_file, "r") as f:
        earliest_time = int(f.readline().strip())
        bus_ids = [each for each in f.readline().strip().split(",")]
    return (earliest_time, bus_ids)


def part_one(earliest_time: int, bus_ids: list[int]) -> int:
    earliest_depart_list = [(id, math.ceil(earliest_time / id) * id) for id in bus_ids]
    earliest_depart_info = min(earliest_depart_list, key=lambda x: x[1])
    bus_id, depart_time = earliest_depart_info
    return bus_id * (depart_time - earliest_time)


def part_two(bus_ids: list[int]) -> int:
    lcm = bus_ids[0]
    ind = 0
    val = bus_ids[ind]
    while ind < len(bus_ids):
        next_ind = ind + 1
        while next_ind < len(bus_ids) and bus_ids[next_ind] == -1:
            next_ind += 1
        if next_ind >= len(bus_ids):
            break
        val, lcm = get_factor(lcm, val, bus_ids[next_ind], next_ind)
        ind = next_ind
    return val


def get_factor(lcm: int, v1: int, v2: int, diff: int) -> tuple[int, int]:
    v = v1 + diff
    while v % v2 != 0:
        v += lcm
    updated_v1 = v - diff
    return updated_v1, math.lcm(lcm, v2)


if __name__ == "__main__":
    input_file = "input/day_13.txt"
    earliest_time, bus_ids = read_input(input_file)

    part_one_bus_ids = [int(id) for id in bus_ids if id != "x"]
    part_one_res = part_one(earliest_time, part_one_bus_ids)
    print(f"{part_one_res=}")

    part_two_bus_ids = [int(id) if id != "x" else -1 for id in bus_ids]
    part_two_res = part_two(part_two_bus_ids)
    print(f"{part_two_res=}")
