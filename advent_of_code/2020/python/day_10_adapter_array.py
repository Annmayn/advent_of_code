import heapq


def read_file(input_file: str) -> list[int]:
    arr: list[int] = [0]
    with open(input_file, "r") as f:
        for val in f:
            arr.append(int(val.strip()))
    arr.sort()
    return arr


def get_diff(arr: list[int]) -> list[int]:
    diff_arr: list[int] = []
    prev_val = arr[0]
    for i in range(1, len(arr)):
        val = arr[i]
        diff_arr.append(val - prev_val)
        prev_val = val
    return diff_arr + [3]


# def read_file(input_file: str) -> list[int]:
#     arr: list[int] = []
#     with open(input_file, "r") as f:
#         for val in f:
#             heapq.heappush(arr, int(val.strip()))
#     diff_arr: list[int] = []
#     prev_val = 0
#     while True:
#         try:
#             val = heapq.heappop(arr)
#             diff_arr.append(val - prev_val)
#             prev_val = val
#         except IndexError:
#             break
#     return diff_arr + [3]


def part_one(data: list[int]) -> int:
    data = get_diff(data)
    num_count = {0: 0, 1: 0, 2: 0, 3: 0}
    for diff in data:
        if diff > 3:
            return -1
        num_count[diff] += 1
    return num_count[1] * num_count[3]


def part_two(data: list[int]) -> int:
    src = 0
    memo: dict[int, int] = {}
    res = find_count(src, data, memo)
    return res


def find_count(src: int, data: list[int], memo: dict[int, int]) -> int:
    if src in memo:
        return memo[src]
    if src == len(data) - 1:
        return 1
    tot_count = 0
    for ind in range(src + 1, len(data)):
        diff = data[ind] - data[src]
        if diff <= 3:
            tot_count += find_count(ind, data, memo)
        else:
            break
    memo[src] = tot_count
    return tot_count


if __name__ == "__main__":
    input_file = "input/day_10.txt"
    data = read_file(input_file)

    part_one_res = part_one(data)
    print(f"{part_one_res=}")

    part_two_res = part_two(data)
    print(f"{part_two_res=}")
