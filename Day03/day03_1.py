# Day 03 exercise 1

import day03


my_map = day03.read_map("input\\input.txt")
day03.print_map(my_map)
# move right 3, down 1        
number_trees = day03.go_down_the_slope(my_map, 3, 1)
print(number_trees)