# Day 13 exercise 1

import day13

def read_input(path):
    with open(path) as file:
        first_line = file.readline()
        timestamp = int(first_line.strip())
        second_line = file.readline()
        bus_dict = dict()
        buses = second_line.strip().split(",")
        for bus in buses:
            if bus != "x":
                bus_dict[int(bus)] = list()
    return timestamp, bus_dict

def calculate_all_timestamps(bus_dict, target):
    for key in bus_dict.keys():
        bus_dict = day13.calculate_bus_timestamps(bus_dict, key, target)
    return bus_dict

def calculate_closer_bus(bus_dict, target):
    bus_max_timestamps = list()
    for key in bus_dict.keys():
        bus_max_timestamps.append((key, bus_dict[key][-1]))
    return min(bus_max_timestamps, key=lambda x: x[1])

my_timestamp, my_bus_dict = read_input("input//input.txt")
print(my_timestamp)
print(my_bus_dict)

my_bus_dict = calculate_all_timestamps(my_bus_dict, my_timestamp)
result = calculate_closer_bus(my_bus_dict, my_timestamp)
print(result)
calculated_result = (result[1] - my_timestamp) * result[0]
print(calculated_result)