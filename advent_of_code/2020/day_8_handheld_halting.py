from pydantic import BaseModel


class Instruction(BaseModel):
    command: str
    sign: str
    value: int


def part_one(instruction_set: list[Instruction]):
    is_instr_executed: dict[int, bool] = {}
    acc = 0
    current_pos = 0
    instr_len = len(instruction_set)
    done = False
    while not done:
        if is_instr_executed.get(current_pos):
            done = True
            continue
        is_instr_executed[current_pos] = True
        next_pos_offset, acc_val = handle_instruction(instruction_set[current_pos])
        current_pos += next_pos_offset
        acc += acc_val
        if current_pos == instr_len - 1:
            done = True
    return acc


def part_two(
    current_pos: int,
    instruction_set: list[Instruction],
    is_instr_executed: dict[int, bool],
    can_flip: bool = True,
):
    flipper = {"jmp": "nop", "nop": "jmp"}
    instr_len = len(instruction_set)
    if is_instr_executed.get(current_pos):
        return 0, False
    if current_pos == instr_len:
        return 0, True
    is_instr_executed[current_pos] = True

    instr = instruction_set[current_pos]
    child_instructions: list[tuple[Instruction, bool]] = [(instr, can_flip)]
    if can_flip and instruction_set[current_pos].command in {"jmp", "nop"}:
        instr_copy = instr.copy()
        instr_copy.command = flipper[instr_copy.command]
        child_instructions.append((instr_copy, False))

    for instr, can_flip in child_instructions:
        next_pos_offset, acc_val = handle_instruction(instr)
        new_pos = current_pos + next_pos_offset
        child_acc, is_valid = part_two(
            new_pos, instruction_set, is_instr_executed, can_flip
        )
        if is_valid:
            acc_val += child_acc
            return acc_val, True
    return 0, False


def handle_instruction(instr: Instruction) -> tuple[int, int]:
    acc = 0
    next_pos_offset = 0
    if instr.command == "acc":
        if instr.sign == "+":
            acc += instr.value
        elif instr.sign == "-":
            acc -= instr.value
        next_pos_offset += 1
    elif instr.command == "nop":
        next_pos_offset += 1
    elif instr.command == "jmp":
        if instr.sign == "+":
            next_pos_offset += instr.value
        elif instr.sign == "-":
            next_pos_offset -= instr.value
    else:
        print("Undefined operation. Skipping...")
    return next_pos_offset, acc


def get_instruction(input_file: str) -> list[Instruction]:
    instruction_set: list[Instruction] = []
    with open(input_file, "r") as f:
        for row in f:
            cmd, val = row.strip().split()
            sign = val[0]
            num = int(val[1:])
            instruction_set.append(Instruction(command=cmd, sign=sign, value=num))
    return instruction_set


if __name__ == "__main__":
    input_file = "input/day_8.txt"
    instruction_set = get_instruction(input_file)
    part_one_res = part_one(instruction_set)
    print(f"{part_one_res=}")

    current_pos = 0
    is_instr_executed: dict[int, bool] = {}
    part_two_res, _ = part_two(current_pos, instruction_set, is_instr_executed)
    print(f"{part_two_res=}")
