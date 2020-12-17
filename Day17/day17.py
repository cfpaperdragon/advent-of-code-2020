# Day 17 common

# taking exercise 11 code as base, which was also about maps
# need to extend it to z
# because we will grow to all 3 directions, we may need to change this a bit
# map[z] = map[y] = maz[x] = (current_state, next_state)
# we know it will run for 6 cycles so we can already extend it 6 times in each direction
# or we'll extend as it goes

def read_map(path):
    map_z = dict()
    map_y = dict()
    with open(path) as file:
        line = file.readline()
        count = 0
        while line:
            map_x = dict()
            for i in range(len(line.strip())):
                position = (line[i], "")
                map_x[i] = position
            map_y[count] = map_x
            line = file.readline()
            count += 1
    map_z[0] = map_y
    return map_z

def print_map(outer_map):
    ykeys = list(outer_map[0].keys())
    ykeys.sort()
    xkeys = list(outer_map[0][0].keys())
    xkeys.sort()
    zkeys = list(outer_map.keys())
    zkeys.sort()
    for k in zkeys:
        print("z = {}".format(k))
        map_dict = outer_map[k]
        for ykey in ykeys:
            line_string = ""
            for xkey in xkeys:
                line_string += map_dict[ykey][xkey][0]
            print(line_string)

def extend_map_z(full_map, z):
    ykeys = full_map[0].keys()
    xkeys = full_map[0][0].keys()
    new_map_y = dict()
    for ykey in ykeys:
        new_map_x = dict()
        for xkey in xkeys:
            new_map_x[xkey] = (".", "")
        new_map_y[ykey] = new_map_x
    full_map[z] = new_map_y

def extend_map_y(full_map, y):
    xkeys = full_map[0][0].keys()
    for zkey in full_map.keys():
        new_map_x = dict()
        for xkey in xkeys:
            new_map_x[xkey] = (".", "")
        full_map[zkey][y] = new_map_x

def extend_map_x(full_map, x):
    for zkey in full_map.keys():
        for ykey in full_map[zkey].keys():
            full_map[zkey][ykey][x] = (".", "")

def check_adjacent_3d(full_map, x, y, z):
    count = 0
    # for z-1, need to check all 9 positions in the square
    if z-1 in full_map.keys():
        count += check_adjacent(full_map, x, y, z-1, True)
    
    # for z, need to check 8 positions surrounding (x,y)
    count += check_adjacent(full_map, x, y, z, False)
    
    # for z+1, need to check all 9 positions in the square
    if z+1 in full_map.keys():
        count += check_adjacent(full_map, x, y, z+1, True)

    return count

def check_adjacent(full_map, x, y, z, check_center):
    # there are 8 possible positions around (x, y) and sometimes we need to check the center
    count = 0
    debug = False
    # top left
    if y-1 in full_map[z].keys():
        if x-1 in full_map[z][y-1].keys():
            if debug:
                print("top left x:{}, y:{}, z:{}, value:{}".format(x-1, y-1, z, full_map[z][y-1][x-1][0]))
            if full_map[z][y-1][x-1][0] == "#":
                count += 1
        else:
            extend_map_x(full_map, x-1)
    else:
        extend_map_y(full_map, y-1)
    
    # top
    if y-1 in full_map[z].keys():
        if debug:
            print("top x:{}, y:{}, z:{}, value:{}".format(x, y-1, z, full_map[z][y-1][x][0]))
        if full_map[z][y-1][x][0] == "#":
            count += 1
    else:
        extend_map_y(full_map, y-1)

    # top right
    if y-1 in full_map[z].keys():
        if x+1 in full_map[z][y-1].keys():
            if debug:
                print("top right x:{}, y:{}, z:{}, value:{}".format(x+1, y-1, z, full_map[z][y-1][x+1][0]))
            if full_map[z][y-1][x+1][0] == "#":
                count += 1
        else:
            extend_map_x(full_map, x+1)
    else:
        extend_map_y(full_map, y-1)
        
    # right
    if x+1 in full_map[z][y].keys():
        if debug:
            print("right x:{}, y:{}, z:{}, value:{}".format(x+1, y, z, full_map[z][y][x+1][0]))
        if full_map[z][y][x+1][0] == "#":
            count += 1
    else:
        extend_map_x(full_map, x+1)

    # bottom right
    if y+1 in full_map[z].keys():
        if x+1 in full_map[z][y+1].keys():
            if debug:
                print("bottom right x:{}, y:{}, z:{}, value:{}".format(x+1, y+1, z, full_map[z][y+1][x+1][0]))
            if full_map[z][y+1][x+1][0] == "#":
                count += 1
        else:
            extend_map_x(full_map, x+1)
    else:
        extend_map_y(full_map, y+1)

    # bottom
    if y+1 in full_map[z].keys():
        if debug:
                print("bottom x:{}, y:{}, z:{}, value:{}".format(x, y+1, z, full_map[z][y+1][x][0]))
        if full_map[z][y+1][x][0] == "#":
            count += 1
    else:
        extend_map_y(full_map, y+1)

    # bottom left
    if y+1 in full_map[z].keys():
        if x-1 in full_map[z][y+1].keys():
            if debug:
                print("bottom left x:{}, y:{}, z:{}, value:{}".format(x-1, y+1, z, full_map[z][y+1][x-1][0]))
            if full_map[z][y+1][x-1][0] == "#":
                count += 1
        else:
            extend_map_x(full_map, x-1)
    else:
        extend_map_y(full_map, y+1)
    
    # left
    if x-1 in full_map[z][y].keys():
        if debug:
            print("left x:{}, y:{}, z:{}, value:{}".format(x-1, y, z, full_map[z][y][x-1][0]))
        if full_map[z][y][x-1][0] == "#":
            count += 1
    else:
        extend_map_x(full_map, x-1)

    # center
    if check_center:
        if debug:
                print("centert x:{}, y:{}, z:{}, value:{}".format(x, y, z, full_map[z][y][x][0]))
        if full_map[z][y][x][0] == "#":
            count += 1

    # print("x:{}, y:{}, z:{}, count:{}".format(x, y, z, count))
    return count
        

def mark_map(m):
    zkeys = list(m.keys())
    ykeys = list(m[0].keys())
    xkeys = list(m[0][0].keys())
    for zkey in zkeys:
        for ykey in ykeys:
            for xkey in xkeys:
                num_adjacent = check_adjacent_3d(m, xkey, ykey, zkey)
                if m[zkey][ykey][xkey][0] == "#":
                    if not (num_adjacent == 2 or num_adjacent == 3):
                        m[zkey][ykey][xkey] = ("#", ".")
                else:
                    if num_adjacent == 3:
                        m[zkey][ykey][xkey] = (".", "#")


def change_map(m):
    count_changes = 0
    zkeys = m.keys()
    ykeys = m[0].keys()
    xkeys = m[0][0].keys()
    for zkey in zkeys:
        for ykey in ykeys:
            for xkey in xkeys:
                if m[zkey][ykey][xkey][1] != "":
                    m[zkey][ykey][xkey] = (m[zkey][ykey][xkey][1], "")
                    count_changes += 1
    return count_changes

def count_map(m):
    count = 0
    zkeys = m.keys()
    ykeys = m[0].keys()
    xkeys = m[0][0].keys()
    for zkey in zkeys:
        for ykey in ykeys:
            for xkey in xkeys:
                if m[zkey][ykey][xkey][0] == "#":
                    count += 1
    return count

def extend_all_directions(m):
    max_x = max(m[0][0].keys())
    min_x = min(m[0][0].keys())
    max_y = max(m[0].keys())
    min_y = min(m[0].keys())
    max_z = max(m.keys())
    min_z = min(m.keys())
    extend_map_x(m, max_x+1)
    extend_map_x(m, min_x-1)
    extend_map_y(m, max_y+1)
    extend_map_y(m, min_y-1)
    extend_map_z(m, max_z+1)
    extend_map_z(m, min_z-1)

