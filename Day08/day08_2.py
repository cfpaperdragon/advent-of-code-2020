# Day 08 exercise 2

import day08

def change_program(last_changed, program_list):
    program_length = len(program_list)

    # find first jump or nop
    changed_code_index = last_changed
    for i in range(last_changed, program_length):
        if program_list[i][0] == "jmp":
            # replace with nop
            changed_code_index = i
            program_list[i] = ("nop", program_list[i][1])
            break
        elif program_list[i][0] == "nop":
            # replace with jmp
            changed_code_index = i
            program_list[i] = ("jmp", program_list[i][1])
            break
        else:
            continue
    return changed_code_index, program_list



program = day08.read_program("input//input.txt")
# program is a list of instructions
# print(program)
index, program = change_program(0, program)
# print(index)
# print(program)

while index < len(program):
    # print(index)
    result = day08.execute_program(program, 0)
    # print(result)
    if result[1]:
        print(result[0])
        break
    else:
        # reset program
        program = program = day08.read_program("input//input.txt")
        index, program = change_program(index+1, program)
        continue
        