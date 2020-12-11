# Day 11 exercise 1

import day11

seat_map = day11.read_map("input//input.txt")

iteractions = 5
changes = 1
while changes > 0:
    iteractions -= 1
    day11.mark_map(seat_map)
    changes = day11.change_map(seat_map)
    
    # check_adjacent(seat_map, 8, 3, "#")

# print_map(seat_map)
count_occupied = day11.count_map(seat_map, "#")
print(count_occupied)
