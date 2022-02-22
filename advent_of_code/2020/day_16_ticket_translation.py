import re
from collections import defaultdict
from typing import Iterator

FieldRange = list[set[int]]
Ticket = list[int]
Memo = dict[int, set[int]]


def read_input(input_file: str) -> tuple[FieldRange, Ticket, list[Ticket]]:
    with open(input_file, "r") as f:
        valid_field_range = read_field_range(f)
        ticket = read_ticket(f)
        nearby_tickets = read_nearby_tickets(f)
    return (valid_field_range, ticket, nearby_tickets)


def read_field_range(f: Iterator[str]) -> FieldRange:
    valid_fields: list[set[int]] = []
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
            valid_range = set(range(s1, e1 + 1)).union(set(range(s2, e2 + 1)))
        valid_fields.append(valid_range)
    return valid_fields


def read_ticket(f: Iterator[str]) -> Ticket:
    next(f)
    ticket = list(map(int, next(f).strip().split(",")))
    next(f)
    return ticket


def read_nearby_tickets(f: Iterator[str]) -> list[Ticket]:
    next(f)
    nearby_tickets = []
    for row in f:
        nearby_tickets.append(list(map(int, row.strip().split(","))))
    return nearby_tickets


def part_one(valid_fields, nearby_tickets):
    sum = 0
    for ticket in nearby_tickets:
        for num in ticket:
            is_invalid = True
            for column in valid_fields:
                if num in column:
                    is_invalid = False
                    break
            if is_invalid:
                sum += num

    return sum


def part_two(
    valid_fields: FieldRange, ticket: Ticket, nearby_tickets: list[Ticket]
) -> int:
    class_map = get_valid_tickets_with_class(valid_fields, nearby_tickets)
    departure_mult = 1
    for i in range(0, 6):
        departure_mult *= ticket[class_map[i]]
    return departure_mult


def get_valid_tickets_with_class(
    valid_fields: FieldRange, nearby_tickets: list[Ticket]
) -> dict[int, int]:
    memo: Memo = {}
    for ticket in nearby_tickets:
        update_range(ticket, valid_fields, memo)

    class_map = remove_duplicates(memo)
    return class_map


def update_range(ticket: Ticket, valid_fields: FieldRange, memo: Memo):
    ticket_memo = defaultdict(set)
    invalid_f = [True] * len(ticket)
    for t_ind, n in enumerate(ticket):
        for ind, field in enumerate(valid_fields):
            if n in field:
                ticket_memo[ind].add(t_ind)
                invalid_f[t_ind] = False

    if any(invalid_f):
        return

    for c_k, t_set in ticket_memo.items():
        if c_k not in memo:
            memo[c_k] = t_set
        else:
            memo[c_k] = memo[c_k].intersection(t_set)


def remove_duplicates(memo: Memo) -> dict[int, int]:
    new_memo: dict[int, int] = {}
    done = False
    while not done:
        done = True
        for k, v in memo.items():
            if len(memo[k]) > 0:
                done = False
            if len(memo[k]) == 1:
                val = v.pop()
                new_memo[k] = val
                remove_all(val, memo)
    return new_memo


def remove_all(v: int, memo: Memo):
    for v_set in memo.values():
        if v in v_set:
            v_set.remove(v)


if __name__ == "__main__":
    input_file = "input/day_16.txt"
    valid_fields, ticket, nearby_tickets = read_input(input_file)

    part_one_res = part_one(valid_fields, nearby_tickets)
    print(f"{part_one_res=}")

    part_two_res = part_two(valid_fields, ticket, nearby_tickets)
    print(f"{part_two_res=}")
