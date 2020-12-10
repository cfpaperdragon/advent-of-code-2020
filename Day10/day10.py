# Day 10 common

def read_input_ints(path):
    input_list = list()
    with open(path) as file:
        line = file.readline()
        while line:
            input_list.append(int(line.strip()))
            line = file.readline()
    return input_list

def print_list(l):
    for i in range(len(l)):
        print(l[i])