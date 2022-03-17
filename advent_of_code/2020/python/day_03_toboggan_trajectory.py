def part_one(input_file):
    graph = get_matrix(input_file)
    tree_count = traverse_graph_part_one(graph)
    print(f"Part 1: {tree_count=}")


def part_two(input_file):
    graph = get_matrix(input_file)
    tree_count = traverse_graph_part_two(graph)
    print(f"Part 2: {tree_count=}")


def get_matrix(input_file: str) -> list[list[str]]:
    graph = []
    with open(input_file, "r") as f:
        for row in f:
            graph.append(list(row.rstrip()))
    return graph


def traverse_graph_part_one(graph: list[list[str]]) -> int:
    tree = "#"
    current_node = (0, 0)
    if not graph:
        return 0
    counter = 0
    num_row = len(graph)
    num_col = len(graph[0])
    while current_node[0] != num_row:
        (r, c) = current_node
        if graph[r][c] == tree:
            counter += 1
        current_node = next_node(current_node, num_col, add_row=1, add_col=3)
    return counter


def traverse_graph_part_two(graph: list[list[str]]) -> int:
    tree = "#"
    if not graph:
        return 0
    num_row = len(graph)
    num_col = len(graph[0])
    add_row_col_info = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    prod = 1
    for add_row, add_col in add_row_col_info:
        counter = 0
        current_node = (0, 0)
        while current_node[0] < num_row:
            (r, c) = current_node
            if graph[r][c] == tree:
                counter += 1
            current_node = next_node(current_node, num_col, add_row, add_col)
        prod *= counter
    return prod


def next_node(
    current: tuple[int, int], max_col: int, add_row: int, add_col: int
) -> tuple[int, int]:
    new_row = current[0] + add_row
    new_col = current[1] + add_col
    if new_col >= max_col:
        new_col %= max_col
    return (new_row, new_col)


if __name__ == "__main__":
    input_file = "input/day_3.txt"
    part_one(input_file)
    part_two(input_file)
