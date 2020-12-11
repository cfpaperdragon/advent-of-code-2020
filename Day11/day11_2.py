# Day 11 exercise 2

import day11

def visible_in_line(map, istart, jstart, irule, jrule, ilimit, jlimit):
    # print("istart:{}, jstart:{}, irule:{}, jrule:{}, ilimit:{}, jlimit:{}".format(
    #      istart, jstart, irule, jrule, ilimit, jlimit
    # ))
    i = istart + irule
    j = jstart + jrule
    result = False
    while i != ilimit and j != jlimit:
        # print("i:{}, j:{}".format(i,j))
        if map[i][j][0] == ".":
            i += irule
            j += jrule
            continue
        elif map[i][j][0] == "L":
            result = False
            break
        elif map[i][j][0] == "#":
            result = True
            break
    # print(result)
    return result

def check_visible(map, ipos, jpos):
    # there are 8 possible directions to check for visible seats
    count = 0
    # top left
    if visible_in_line(map, ipos, jpos, -1, -1, -1, -1):
        count += 1
    # top
    if visible_in_line(map, ipos, jpos, -1, 0, -1, -1):
        count += 1
    # top right
    if visible_in_line(map, ipos, jpos, -1, +1, -1, len(map[0])):
        count += 1
    # right
    if visible_in_line(map, ipos, jpos, 0, +1, -1, len(map[0])):
        count += 1
    # bottom right
    if visible_in_line(map, ipos, jpos, +1, +1, len(map.keys()), len(map[0])):
        count += 1
    # bottom
    if visible_in_line(map, ipos, jpos, +1, 0, len(map.keys()), -1):
        count += 1
    # bottom left
    if visible_in_line(map, ipos, jpos, +1, -1, len(map.keys()), -1):
        count += 1
    # left
    if visible_in_line(map, ipos, jpos, 0, -1, -1, -1):
        count += 1
    # print("i={}, j={}, count={}".format(ipos, jpos, count))
    return count
    

def new_mark_map(m):
    for i in range(len(m.keys())):
        for j in range(len(m[i])):
            if m[i][j][0] == "L":
                if check_visible(m, i, j) == 0:
                    m[i][j] = ("L", "#")
            elif m[i][j][0] == "#":
                if check_visible(m, i, j) >= 5:
                    m[i][j] = ("#", "L")

seat_map = day11.read_map("input//input.txt")

iteractions = 3
changes = 1
while changes > 0:
    iteractions -= 1
    new_mark_map(seat_map)
    changes = day11.change_map(seat_map)
    
    # check_adjacent(seat_map, 8, 3, "#")

# visible_in_line(seat_map, 0, 0, 1, 1, 10, 10)
# day11.print_map(seat_map)
# check_visible(seat_map, 0, 3)
count_occupied = day11.count_map(seat_map, "#")
print(count_occupied)
