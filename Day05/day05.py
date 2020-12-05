# Day05 common

def read_input(path):
    input_list = list()
    with open(path) as file:
        line = file.readline()
        while line:
            input_list.append(line.strip())
            line = file.readline()
    return input_list

def decode_boardingpass_row(bp):
    min_row = 0
    max_row = 127
    mid_row_front = 63
    mid_row_back = 64
    for i in range(7):
        if bp[i] == "F":
            # min_row is kept
            # max_row will be mid_row
            max_row = mid_row_front
            # new mid_row will be between min_row and new max_row       
        else:
            # max_row is kept
            # min_row will be mid_row
            min_row = mid_row_back
            # new mid_row will be between new min_row and max_row
        mid_row_front = min_row + (max_row - min_row) // 2
        mid_row_back = mid_row_front + 1 
        # print("min_row={}, max_row={}, mid_row_front={}, mid_row_back={}".format(min_row, max_row, mid_row_front, mid_row_back))
    return min_row

def decode_boardingpass_column(bp):
    min_col = 0
    max_col = 7
    mid_col_front = 3
    mid_col_back = 4
    for i in range(7,10):
        if bp[i] == "L":
            # min_col is kept
            max_col = mid_col_front
        else:
            # max col is kept
            min_col = mid_col_back
        mid_col_front = min_col + (max_col - min_col) // 2
        mid_col_back = mid_col_front + 1
        # print("min_col={}, max_col={}, mid_col_front={}, mid_col_back={}".format(min_col, max_col, mid_col_front, mid_col_back))
    return min_col