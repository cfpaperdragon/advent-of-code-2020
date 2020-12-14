# Day 14 exercise 1

import day14

program = day14.read_input("input//input.txt")

# print(program)

memory = day14.execute(program)
sum = 0
for key in memory.keys():
    sum += memory[key]
print(sum)
