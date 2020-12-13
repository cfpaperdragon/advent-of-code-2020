# Day 13 exercise 2

def read_input(path):
    with open(path) as file:
        file.readline()
        second_line = file.readline()
        bus_dict = dict()
        bus_list = list()
        buses = second_line.strip().split(",")
        for bus in buses:
            bus_list.append(bus)
            if bus != "x":
                bus_dict[int(bus)] = list()
    return bus_list, bus_dict

def calculate_next_bus(bus_dict):
    for key in bus_dict.keys():
        bus_dict[key].append(key*len(bus_dict[key]))

def find_timestamp(bus_dict, bus_list, start_value, step):
    t = start_value
    next_step = step 


    while True:
        accumulator = 1
        for i in range(0, len(my_bus_list)):
            if my_bus_list[i] == "x":
                continue
            i_bus = int(my_bus_list[i])
            if (t + i) % i_bus == 0:
                bus_dict[i_bus].append(t+i)
                accumulator *= i_bus
                # print("timestamp:{}, i:{}, i_bus:{}, accumulator:{}".format(t, i, i_bus, accumulator))
                if i == len(my_bus_list)-1:
                    # we reached the target
                    # print("t:{}, bus_dict:{}".format(t, bus_dict))
                    # for key in bus_dict.keys():
                    #     print("key:{}, last 5:{}".format(key, bus_dict[key][-5:]))
                    return t
            else: 
                next_step = accumulator - i              
                break
        t += next_step
    return t


my_bus_list, my_bus_dict = read_input("input//input.txt")

result = find_timestamp(my_bus_dict, my_bus_list, 0, 1)
print(result)