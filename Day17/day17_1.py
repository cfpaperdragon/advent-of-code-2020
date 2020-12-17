# Day 17 exercise 1

import day17

full_map = day17.read_map("input//input.txt")

day17.print_map(full_map)

cycle = 6
while cycle > 0:
    cycle -= 1
    day17.extend_all_directions(full_map)
    day17.mark_map(full_map)
    day17.change_map(full_map)


# result = check_adjacent_3d(full_map, 0, 0, 0)
# print(result)

# print_map(full_map)
result = day17.count_map(full_map)
print(result)
