# Day 11 exercise 1

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

def init_map(m):
    for i in range(len(m.keys())):
        for j in range(len(m[i])):
            if m[i][j][0] == "L":
                m[i][j] = ("#", "")

def check_at_least_n_adjacent(map, ipos, jpos, n, char_value):
    # there are 8 possible positions around (ipos, jpos)
    count = 0
    # top left
    if ipos > 1 and jpos > 1: 
        if map[ipos-1][jpos-1][0] == char_value:
            count += 1
    # top
    if ipos > 1:
        if map[ipos-1][jpos][0] == char_value:
            count += 1
    # top right
    if ipos > 1 and jpos < len(map[0]) - 1:
        if map[ipos-1][jpos+1][0] == char_value:
            count += 1
    # right
    if jpos < len(map[0]) - 1:
        if map[ipos][jpos+1][0] == char_value:
            count += 1
    # bottom right
    if ipos < len(map.keys())-1 and jpos < len(map[0]) - 1:
        if map[ipos+1][jpos+1][0] == char_value:
            count += 1
    # bottom
    if ipos < len(map.keys())-1:
        if map[ipos+1][jpos][0] == char_value:
            count += 1
    # bottom left
    if ipos < len(map.keys())-1 and jpos > 1:
        if map[ipos+1][jpos-1][0] == char_value:
            count += 1
    # left
    if ipos > 1:
        if map[ipos-1][jpos][0] == char_value:
            count += 1

    return count >= n
        

def mark_map(m):
    for i in range(len(m.keys())):
        for j in range(len(m[i])):
            if m[i][j][0] == "L":
                if not check_at_least_n_adjacent(m, i, j, 1, "#"):
                    m[i][j] = ("L", "#")
            elif m[i][j][0] == "#":
                if check_at_least_n_adjacent(m, i, j, 4, "#"):
                    m[i][j] = ("#", "L")

def change_map(m):
    count_changes = 0
    for i in range(len(m.keys())):
        for j in range(len(m[i])):
            if m[i][j][1] != "":
                m[i][j] = (m[i][j][1], "")
                count_changes += 1
    return count_changes


seat_map = read_map("input//example.txt")
# print_map(seat_map)
init_map(seat_map)
# print_map(seat_map)
mark_map(seat_map)
changes = change_map(seat_map)
print(changes)
print_map(seat_map)