# Day 09 exercise 2

import day09

def find_sequence_limits(nl, bottom_pos, value):
    # since we have big numbers down the list, smaller numbers up the list, going to do this down -> up
    start_pos = bottom_pos
    while start_pos > 0:
        sequence_sum = 0
        start_pos -= 1
        for i in range(start_pos, 1, -1):
            sequence_sum += nl[i]
            if sequence_sum == value:
                return (i, start_pos)
            elif sequence_sum > value:
                # reset
                break
    return 0
                



number_list = day09.read_input_ints("input//input.txt")

result = day09.first_invalid(number_list, 25)

result_index = result[0]
result_value = result[1]

sequence_limits = find_sequence_limits(number_list, result_index, result_value)
# print(sequence_limits)
top_limit = sequence_limits[0]
bottom_limit = sequence_limits[1]

sequence = number_list[top_limit:bottom_limit+1]
# print(sequence)
max_value = max(sequence)
min_value = min(sequence)
print("min={}, max={}, result={}".format(min_value, max_value, min_value + max_value))