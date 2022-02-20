import re


def read_input(input_file: str) -> tuple[set, list, list]:
    with open(input_file, "r") as f:
        valid_field_range = read_field_range(f)
        ticket = read_ticket(f)
        nearby_tickets = read_nearby_tickets(f)
    return (valid_field_range, ticket, nearby_tickets)


def read_field_range(f) -> set:
    valid_fields = set()
    for row in f:
        if row.strip() == "":
            break
        row_pattern = r".*?:\s+(?P<s1>\d+)-(?P<e1>\d+)\s+or\s+(?P<s2>\d+)-(?P<e2>\d+)"
        res = re.match(row_pattern, row.strip())
        valid_range = set()
        if res is not None:
            res_dict = res.groupdict()
            s1 = int(res_dict["s1"])
            e1 = int(res_dict["e1"])
            s2 = int(res_dict["s2"])
            e2 = int(res_dict["e2"])
            valid_range = {*list(range(s1, e1 + 1)), *list(range(s2, e2 + 1))}
        valid_fields = valid_fields.union(valid_range)
    return valid_fields


def read_ticket(f):
    next(f)
    ticket = list(map(int, next(f).strip().split(",")))
    next(f)
    return ticket


def read_nearby_tickets(f):
    next(f)
    nearby_tickets = []
    for row in f:
        nearby_tickets.append(list(map(int, row.strip().split(","))))
    return nearby_tickets


def part_one(valid_fields, nearby_tickets):
    sum = 0
    for ticket in nearby_tickets:
        for num in ticket:
            if num not in valid_fields:
                sum += num
    return sum


if __name__ == "__main__":
    input_file = "input/day_16.txt"
    valid_fields, ticket, nearby_tickets = read_input(input_file)

    part_one_res = part_one(valid_fields, nearby_tickets)
    print(f"{part_one_res=}")
