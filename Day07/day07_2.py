# Day 07 exercise 2

import day07

def count_bags_inside(contains_dict, color):
    # print(color)
    if color not in contains_dict:
        return 0
    else:
        contained_list = contains_dict[color]
        # print(contained_list)
        if len(contained_list) == 0:
            return 0
        result = 0
        for contained in contained_list:
            result += contained[0] + contained[0] * count_bags_inside(contains_dict, contained[1])
        return result

contains, is_contained = day07.read_dictionaries("input\\input.txt")

# day07.pretty_print_dict("contains", contains)

number_bags = count_bags_inside(contains, "shiny gold")
print(number_bags)
