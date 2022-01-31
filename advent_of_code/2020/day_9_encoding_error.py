from collections import deque


def read_input(input_file: str) -> list[int]:
    with open(input_file, "r") as f:
        data = [int(each) for each in f]
    return data


def part_one(data: list[int], preamble_len: int = 25) -> int:
    for i, ind in enumerate(range(preamble_len, len(data))):
        sliced_arr = data[i : i + preamble_len]
        if not can_sum(sliced_arr, data[ind]):
            return data[ind]
    return -1


def part_two(data: list[int], target: int) -> int:
    start_ind = 0
    res_arr = find_arr(data, target)
    if res_arr:
        res_arr.sort()
        return res_arr[0] + res_arr[-1]
    return -1


def can_sum(arr: list[int], target: int) -> bool:
    complement_arr = set()
    for each in arr:
        if each <= target:
            complement = target - each
            if complement in complement_arr:
                return True
            complement_arr.add(each)
    return False


def find_arr(data: list[int], target: int) -> list[int]:
    done = False
    ind = 0
    que: deque[int] = deque()
    while not done:
        while sum(que) < target:
            que.append(data[ind])
            ind += 1
        if sum(que) == target:
            return list(que)
        while sum(que) > target:
            que.popleft()
        if ind == len(data):
            done = True
    return []


if __name__ == "__main__":
    input_file = "input/day_9.txt"
    data = read_input(input_file)

    part_one_res = part_one(data)
    print(f"{part_one_res=}")

    part_two_res = part_two(data, part_one_res)
    print(f"{part_two_res=}")
