# Day 18 common

def read_input(path):
    with open(path) as file:
        input_list = list()
        line = file.readline()
        while line:
            input_list.append(line.strip())
            line = file.readline()
    return input_list