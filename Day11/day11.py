# Day 11 common

def read_map(path):
    map = dict()
    with open(path) as file:
        line = file.readline()
        count = 0
        while line:
            line_list = list()
            for i in range(len(line.strip())):
                position = (line[i], "")
                line_list.append(position)
            map[count] = line_list
            line = file.readline()
            count += 1
    return map

def print_map(map_dict):
    for i in range(len(map_dict.keys())):
        line_string = ""
        for j in range(len(map_dict[i])):
            line_string += map_dict[i][j][0]
        print(line_string)

def print_real_map(map_dict):
    for i in range(len(map_dict.keys())):
        print(map_dict[i])

def init_map(m):
    for i in range(len(m.keys())):
        for j in range(len(m[i])):
            if m[i][j][0] == "L":
                m[i][j] = ("#", "")

def check_adjacent(map, ipos, jpos, char_value):
    # there are 8 possible positions around (ipos, jpos)
    count = 0
    # top left
    if ipos >= 1 and jpos >= 1:
        # print("top left: i-1, j-1:" + map[ipos-1][jpos-1][0]) 
        if map[ipos-1][jpos-1][0] == char_value:
            count += 1
    # top
    if ipos >= 1:
        # print("top i-1, j: " + map[ipos-1][jpos][0])
        if map[ipos-1][jpos][0] == char_value:
            count += 1
    # top right
    if ipos >= 1 and jpos < len(map[0]) - 1:
        # print("top right i-1, j+1: " + map[ipos-1][jpos+1][0])
        if map[ipos-1][jpos+1][0] == char_value:
            count += 1
    # right
    if jpos < len(map[0]) - 1:
        # print("right i, j+1: " + map[ipos][jpos+1][0])
        if map[ipos][jpos+1][0] == char_value:
            count += 1
    # bottom right
    if ipos < len(map.keys())-1 and jpos < len(map[0]) - 1:
        # print("bottom right i+1, j+1: " + map[ipos+1][jpos+1][0])
        if map[ipos+1][jpos+1][0] == char_value:
            count += 1
    # bottom
    if ipos < len(map.keys())-1:
        # print("bottom i+1, j: " + map[ipos+1][jpos][0])
        if map[ipos+1][jpos][0] == char_value:
            count += 1
    # bottom left
    if ipos < len(map.keys())-1 and jpos >= 1:
        # print("bottom left i+1, j-1: " + map[ipos+1][jpos-1][0])
        if map[ipos+1][jpos-1][0] == char_value:
            count += 1
    # left
    if jpos >= 1:
        # print("left i, j-1: " + map[ipos][jpos-1][0])
        if map[ipos][jpos-1][0] == char_value:
            count += 1

    # print("i={}, j={}, count={}".format(ipos, jpos, count))
    return count
        

def mark_map(m):
    for i in range(len(m.keys())):
        for j in range(len(m[i])):
            if m[i][j][0] == "L":
                if check_adjacent(m, i, j, "#") == 0:
                    m[i][j] = ("L", "#")
            elif m[i][j][0] == "#":
                if check_adjacent(m, i, j, "#") >= 4:
                    m[i][j] = ("#", "L")

def change_map(m):
    count_changes = 0
    for i in range(len(m.keys())):
        for j in range(len(m[i])):
            if m[i][j][1] != "":
                m[i][j] = (m[i][j][1], "")
                count_changes += 1
    return count_changes

def count_map(m, char_value):
    count = 0
    for i in range(len(m.keys())):
        for j in range(len(m[i])):
            if m[i][j][0] == char_value:
                count += 1
    return count