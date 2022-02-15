def read_input(input_file: str) -> list[int]:
    with open(input_file, 'r') as f:
        data = f.read()
    return list(map(int, data.strip().split(',')))

def part_one(data: list[int]):
    val_to_ind_map: dict[int, int] = {k: i for i, k in enumerate(data)}
    curr_val = 0
    curr_ind = len(data)
    while (curr_ind + 1) != 2020:
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

    part_one_res = part_one(data)
    print(f"{part_one_res=}")
