# Day 08 common

def parse_line(l):
    split_line = l.strip().split(" ")
    return (split_line[0], int(split_line[1]))
    

def read_program(path):
    input_list = list()
    with open(path) as file:
        line = file.readline()
        while line:
            parsed = parse_line(line)
            input_list.append(parsed)
            line = file.readline()
    return input_list


def execute_program(program, accumulator):
    visited = list()
    instruction_index = 0
    while instruction_index < len(program):
        if instruction_index in visited:
            return accumulator, False
        else:
            visited.append(instruction_index)

        instruction = program[instruction_index]
        instruction_name = instruction[0]
        if instruction_name == "acc":
            accumulator += instruction[1]
            instruction_index += 1
        elif instruction_name == "jmp":
            instruction_index += instruction[1]
        elif instruction_name == "nop":
            instruction_index += 1
        else:
            # invalid instruction
            return accumulator, False
    return accumulator, True