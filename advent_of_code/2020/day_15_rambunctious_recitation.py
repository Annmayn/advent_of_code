def read_input(input_file: str) -> list[int]:
    with open(input_file, "r") as f:
        data = f.read()
    return list(map(int, data.strip().split(",")))


def main(data: list[int], n) -> int:
    val_to_ind_map: dict[int, int] = {k: i for i, k in enumerate(data)}
    curr_val = 0
    curr_ind = len(data)
    while (curr_ind + 1) != n:
        if curr_val in val_to_ind_map:
            prev_ind = val_to_ind_map[curr_val]
            val_to_ind_map[curr_val] = curr_ind
            curr_val = curr_ind - prev_ind
        else:
            val_to_ind_map[curr_val] = curr_ind
            curr_val = 0
        curr_ind += 1
    return curr_val


if __name__ == "__main__":
    input_file = "input/day_15.txt"
    data = read_input(input_file)

    part_one_res = main(data, 2020)
    print(f"{part_one_res=}")

    part_two_res = main(data, 30000000)
    print(f"{part_two_res=}")
