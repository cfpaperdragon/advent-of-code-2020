# Day 09 common

def read_input_ints(path):
    input_list = list()
    with open(path) as file:
        line = file.readline()
        while line:
            input_list.append(int(line.strip()))
            line = file.readline()
    return input_list

def valid_number(nl, index, preamble):
    # number at index is valid 
    # if there are 2 numbers in the preamble that added are its value
    value = nl[index]
    for i in range(index - preamble, index):
        for j in range(index - preamble + 1, index):
            if nl[i] + nl[j] == value:
                return True
    return False

def first_invalid(nl, preamble):
    for i in range(preamble, len(nl)):
        if not valid_number(nl, i, preamble):
            return (i, nl[i])
    return 0