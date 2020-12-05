# Day 05 exercise 1

def read_input(path):
    input_list = list()
    with open(path) as file:
        line = file.readline()
        while line:
            input_list.append(line.strip())
            line = file.readline()
    return input_list

def decode_boardingpass(bp):
    # this is kind of binary search
    rows = list(range(0,128))
    min_row = 0
    max_row = 127
    mid_row = 63
    for i in range(7):
        if bp[i] == "F":
            # min_row is kept
            # max_row will be mid_row
            max_row = mid_row
            # new mid_row will be between min_row and new max_row
            mid_row = min_row + (max_row - min_row) // 2 
        else:
            # max_row is kept
            # min_row will be mid_row
            min_row = mid_row
            # new mid_row will be between new min_row and max_row
            mid_row = min_row + (max_row - min_row) // 2 
        print("min_row={}, max_row={}, mid_row={}".format(min_row, max_row, mid_row))
    return mid_row

boardingpass_list = read_input("input//example.txt")
# print(boardingpass_list)
for boardingpass in boardingpass_list:
    print(decode_boardingpass(boardingpass))