# Day 07 exercise 1

import day07

def get_number_bags_with_color(is_contained_dict, color, visited_list):
    # print(color)
    # print(visited_list)
    result = 0
    if color not in visited_list:
        visited_list.append(color)
        result = 1
    else:
        return (result, visited_list)
    if color not in is_contained_dict:
        return (result, visited_list)
    else:
        container_colors = is_contained_dict[color]
        for container_color in container_colors:
            call_result = get_number_bags_with_color(is_contained_dict, container_color, visited_list)
            result += call_result[0]
            visited_list = call_result[1]
        return (result, visited_list)


contains, is_contained = day07.read_dictionaries("input\\input.txt")

# pretty_print_dict("contains", contains)
# pretty_print_dict("is_contained", is_contained)

count_shiny_gold = get_number_bags_with_color(is_contained, "shiny gold", list())
print(count_shiny_gold[0]-1)
