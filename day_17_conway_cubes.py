from typing import Coroutine, Iterator, Union


NDimData = list[list[list[str]]]
Coordinates = tuple[int, int, int]

Coordinates4D = tuple[int, int, int, int]


def read_input(input_file: str) -> NDimData:
    with open(input_file, "r") as f:
        data = [[list(row) for row in f.read().strip().split("\n")]]
        return data


def part_one(data: NDimData, num_runs: int = 6) -> int:
    active_states = get_initial_state(data)
    for _ in range(num_runs):
        active_states = run_cycle(active_states)
    return len(active_states)


def get_initial_state(data: NDimData) -> set[Coordinates]:
    active_states: set[Coordinates] = set()
    for i, grid in enumerate(data):
        for j, row in enumerate(grid):
            for k, col in enumerate(row):
                if col == "#":
                    active_states.add((i, j, k))
    return active_states


def run_cycle(active_states: set[Coordinates]) -> set[Coordinates]:
    new_active_states: set[Coordinates] = set()
    for src in active_states:
        neighbors = get_neighbors(src)
        for node in neighbors:
            active_neighbors = get_active_neighbors(node, active_states)
            if node in active_states:
                if active_neighbors in (2, 3):
                    new_active_states.add(node)
            else:  # inactive
                if active_neighbors == 3:
                    new_active_states.add(node)
    return new_active_states


def get_neighbors(node: Coordinates) -> Iterator[Coordinates]:
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                yield (node[0] + i, node[1] + j, node[2] + k)


def get_active_neighbors(node: Coordinates, active_states: set[Coordinates]) -> int:
    active_neighbors = 0
    for node_neigh in get_neighbors(node):
        if node_neigh != node and node_neigh in active_states:
            active_neighbors += 1
    return active_neighbors


def part_two(data: NDimData, num_runs: int = 6) -> int:
    active_states = get_initial_state_part_two(data)
    for _ in range(num_runs):
        active_states = run_cycle_part_two(active_states)
    return len(active_states)


def get_initial_state_part_two(data: NDimData) -> set[Coordinates4D]:
    active_states: set[Coordinates4D] = set()
    for x in range(1):
        for i, grid in enumerate(data):
            for j, row in enumerate(grid):
                for k, col in enumerate(row):
                    if col == "#":
                        active_states.add((x, i, j, k))
    return active_states


def run_cycle_part_two(active_states: set[Coordinates4D]) -> set[Coordinates4D]:
    new_active_states: set[Coordinates4D] = set()
    for src in active_states:
        neighbors = get_neighbors_part_two(src)
        for node in neighbors:
            active_neighbors = get_active_neighbors_part_two(node, active_states)
            if node in active_states:
                if active_neighbors in (2, 3):
                    new_active_states.add(node)
            else:  # inactive
                if active_neighbors == 3:
                    new_active_states.add(node)
    return new_active_states


def get_neighbors_part_two(node: Coordinates4D) -> Iterator[Coordinates4D]:
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for w in range(-1, 2):
                    yield (node[0] + i, node[1] + j, node[2] + k, node[3] + w)

def get_active_neighbors_part_two(node: Coordinates4D, active_states: set[Coordinates4D]) -> int:
    active_neighbors = 0
    for node_neigh in get_neighbors_part_two(node):
        if node_neigh != node and node_neigh in active_states:
            active_neighbors += 1
    return active_neighbors


if __name__ == "__main__":
    input_file = "input/day_17.txt"
    data = read_input(input_file)

    part_one_res = part_one(data)
    print(f"{part_one_res=}")

    part_two_res = part_two(data)
    print(f"{part_two_res=}")
