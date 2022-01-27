from collections import defaultdict

Graph = dict[str, list[tuple[str, int]]]


def part_one(src: str, graph: Graph, visited: dict[str, bool]) -> int:
    neigh = graph.get(src)
    if neigh is None:
        return 0
    counter = 0
    for (each, _) in neigh:
        if each not in visited:
            visited[each] = True
            counter += 1
            each_counter = part_one(each, graph, visited)
            counter += each_counter
    return counter


def part_two(src: str, graph: Graph, num_bags_needed: dict[str, int]) -> int:
    if src in num_bags_needed:
        return num_bags_needed[src]
    neigh = graph.get(src)
    if neigh is None:
        return 0
    counter = 0
    for (each, num) in neigh:
        counter += num
        each_counter = part_two(each, graph, num_bags_needed)
        num_bags_needed[each] = each_counter
        counter += num * each_counter
    return counter


def build_graph_from_file_part_one(input_file: str) -> Graph:
    graph = defaultdict(list)
    with open(input_file, "r") as f:
        for row in f:
            key, value = row.strip().rstrip(".").split(" contain ")
            key = key.rstrip("s")
            for value in value.split(","):
                value_arr = value.strip().rstrip("s").split(" ")
                bag_name = " ".join(value_arr[1:])
                bag_count = value_arr[0]
                if bag_count != "no":
                    graph[bag_name].append((key, int(bag_count)))
    return graph


def build_graph_from_file_part_two(input_file: str) -> Graph:
    graph = defaultdict(list)
    with open(input_file, "r") as f:
        for row in f:
            key, value = row.strip().rstrip(".").split(" contain ")
            key = key.rstrip("s")
            for value in value.split(","):
                value_arr = value.strip().rstrip("s").split(" ")
                bag_name = " ".join(value_arr[1:])
                bag_count = value_arr[0]
                if bag_count != "no":
                    graph[key].append((bag_name, int(bag_count)))
    return graph


if __name__ == "__main__":
    input_file = "input/day_7.txt"

    graph = build_graph_from_file_part_one(input_file)
    visited: dict[str, bool] = {}
    part_one_res = part_one(src="shiny gold bag", graph=graph, visited=visited)
    print(f"{part_one_res=}")

    graph = build_graph_from_file_part_two(input_file)
    num_bags_needed: dict[str, int] = {}
    part_two_res = part_two(
        src="shiny gold bag", graph=graph, num_bags_needed=num_bags_needed
    )
    print(f"{part_two_res=}")
