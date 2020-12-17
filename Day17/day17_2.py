# Day 17 exercise 2

import day17

# try to extend with another outside map
def print_4d_map(map):
    wkeys = list(map.keys())
    wkeys.sort()
    for wkey in wkeys:
        print("w = {}".format(wkey))
        day17.print_map(map[wkey])

def extend_4d_map_x(map, x):
    for wkey in map.keys():
        day17.extend_map_x(map[wkey], x)

def extend_4d_map_y(map, y):
    for wkey in map.keys():
        day17.extend_map_y(map[wkey], y)

def extend_4d_map_z(map, z):
    for wkey in map.keys():
        day17.extend_map_z(map[wkey], z)

def extend_4d_map_w(map, w):
    zkeys = map[0].keys()
    ykeys = map[0][0].keys()
    xkeys = map[0][0][0].keys()
    new_map_z = dict()
    for zkey in zkeys:
        new_map_y = dict()
        for ykey in ykeys:
            new_map_x = dict()
            for xkey in xkeys:
                new_map_x[xkey] = (".", "")
            new_map_y[ykey] = new_map_x
        new_map_z[zkey] = new_map_y
    map[w] = new_map_z

def get_x_keys(m, sort):
    xkeys = list(m[0][0][0].keys())
    if sort:
        xkeys.sort()
    return xkeys

def get_y_keys(m, sort):
    ykeys = list(m[0][0].keys())
    if sort:
        ykeys.sort()
    return ykeys

def get_z_keys(m, sort):
    zkeys = list(m[0].keys())
    if sort:
        zkeys.sort()
    return zkeys

def get_w_keys(m, sort):
    wkeys = list(m.keys())
    if sort:
        wkeys.sort()
    return wkeys

def count_all_adjacent_map_4d(m, x, y, z, w):
    count = 0
    wkeys = get_w_keys(m, False)
    zkeys = get_z_keys(m, False)
    ykeys = get_y_keys(m, False)
    xkeys = get_x_keys(m, False)
    # if x == 0 and y == 0:
    # print("x:{}, y:{}, z:{}, w:{}".format(x, y, z, w))
    for wkey in range(w-1,w+2):
        for zkey in range(z-1,z+2):
            for ykey in range(y-1,y+2):
                for xkey in range(x-1,x+2):
                    # print("xkey:{}, ykey:{}, zkey:{}, wkey:{}".format(xkey, ykey, zkey, wkey))
                    if wkey in wkeys and zkey in zkeys and ykey in ykeys and xkey in xkeys:
                        # if x==0 and y==0:
                        # print("xkey:{}, ykey:{}, zkey:{}, wkey:{}, value:{}".format(xkey, ykey, zkey, wkey, m[wkey][zkey][ykey][xkey][0]))
                        if not (wkey == w and zkey == z and ykey == y and xkey == x):
                            if m[wkey][zkey][ykey][xkey][0] == "#":
                                count += 1
    # if x==0 and y==0:
    # print(count)
    return count

def extend_all_4_directions(m):
    max_x = max(get_x_keys(m, False))
    min_x = min(get_x_keys(m, False))
    max_y = max(get_y_keys(m, False))
    min_y = min(get_y_keys(m, False))
    max_z = max(get_z_keys(m, False))
    min_z = min(get_z_keys(m, False))
    max_w = max(get_w_keys(m, False))
    min_w = min(get_w_keys(m, False))
    extend_4d_map_x(m, max_x+1)
    extend_4d_map_x(m, min_x-1)
    extend_4d_map_y(m, max_y+1)
    extend_4d_map_y(m, min_y-1)
    extend_4d_map_z(m, max_z+1)
    extend_4d_map_z(m, min_z-1)
    extend_4d_map_w(m, max_w+1)
    extend_4d_map_w(m, min_w-1)

def mark_map(m):
    wkeys = get_w_keys(m, False)
    zkeys = get_z_keys(m, False)
    ykeys = get_y_keys(m, False)
    xkeys = get_x_keys(m, False)
    for wkey in wkeys:
        for zkey in zkeys:
            for ykey in ykeys:
                for xkey in xkeys:
                    num_adjacent = count_all_adjacent_map_4d(m, xkey, ykey, zkey, wkey)
                    if m[wkey][zkey][ykey][xkey][0] == "#":
                        if not (num_adjacent == 2 or num_adjacent == 3):
                            m[wkey][zkey][ykey][xkey] = ("#", ".")
                    else:
                        if num_adjacent == 3:
                            m[wkey][zkey][ykey][xkey] = (".", "#")

def change_map(m):
    count_changes = 0
    wkeys = get_w_keys(m, False)
    zkeys = get_z_keys(m, False)
    ykeys = get_y_keys(m, False)
    xkeys = get_x_keys(m, False)
    for wkey in wkeys:
        for zkey in zkeys:
            for ykey in ykeys:
                for xkey in xkeys:
                    if m[wkey][zkey][ykey][xkey][1] != "":
                        m[wkey][zkey][ykey][xkey] = (m[wkey][zkey][ykey][xkey][1], "")
                        count_changes += 1
    return count_changes

def count_map(m):
    count = 0
    wkeys = get_w_keys(m, False)
    zkeys = get_z_keys(m, False)
    ykeys = get_y_keys(m, False)
    xkeys = get_x_keys(m, False)
    for wkey in wkeys:
        for zkey in zkeys:
            for ykey in ykeys:
                for xkey in xkeys:
                    if m[wkey][zkey][ykey][xkey][0] == "#":
                        count += 1
    return count    

map_3d = day17.read_map("input//input.txt")
map_4d = dict()
map_4d[0] = map_3d

# print_4d_map(map_4d)

cycle = 6
while cycle > 0:
    cycle -= 1
    extend_all_4_directions(map_4d)
    mark_map(map_4d)
    change_map(map_4d)
    # for y in get_y_keys(map_4d, True):
    #     for x in get_x_keys(map_4d, True):
    #         count_all_adjacent_map_4d(map_4d, x, y, -1, -1)

# print_4d_map(map_4d)
result = count_map(map_4d)
print(result)
