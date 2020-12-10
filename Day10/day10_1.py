# Day 10 exercise 1

import day10

def count_differences(l):
    count_differences_1 = 0
    count_differences_3 = 0
    for i in range(1, len(l)):
        if l[i] - l[i-1] == 1:
            count_differences_1 += 1
        elif l[i] - l[i-1] == 3:
            count_differences_3 += 1
    return (count_differences_1, count_differences_3)

def print_list(l):
    for i in range(len(l)):
        print(l[i])


chargers = day10.read_input_ints("input\\input.txt")
chargers.append(0)
chargers.append(max(chargers)+3)
chargers.sort()

# print_list(chargers)

result = count_differences(chargers)
print("differences of 1 = {}, differences of 3 = {}, total = {}".format(result[0], result[1], result[0] * result[1]))