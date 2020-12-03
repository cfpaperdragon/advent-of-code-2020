# Day 03 exercise 2
import day03

my_map = day03.read_map("input\\input.txt")
# day03.print_map(my_map)        
t_1_1 = day03.go_down_the_slope(my_map, 1, 1)
t_3_1 = day03.go_down_the_slope(my_map, 3, 1)
t_5_1 = day03.go_down_the_slope(my_map, 5, 1)
t_7_1 = day03.go_down_the_slope(my_map, 7, 1)
t_1_2 = day03.go_down_the_slope(my_map, 1, 2)
print("{} {} {} {} {} {}".format(t_1_1, t_3_1, t_5_1, t_7_1, t_1_2, t_1_1 * t_3_1 * t_5_1 * t_7_1 * t_1_2))
