# Day 08 exercise 1

import day08

program = day08.read_program("input//input.txt")
# program is a list of instructions

result = day08.execute_program(program, 0)
print(result)