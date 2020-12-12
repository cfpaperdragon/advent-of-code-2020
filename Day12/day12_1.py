# Day 12 exercise 1

import day12

instructions = day12.read_input("input//input.txt")
# print(instructions)

start_x = 0
start_y = 0
start_direction = "E"

result = day12.follow_all_instructions(start_x, start_y, start_direction, instructions)

print(result)
print(abs(result[0])+abs(result[1]))
