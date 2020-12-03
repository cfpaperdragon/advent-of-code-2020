# Day 03 connon

def print_map(m):
    for i in range(len(m)):
        print(m[i])

def check_position(h, v, m, real_h):
    h = h % real_h # reduce to real position
    # print("h={}, v={}, real_h={}".format(h, v, real_h))
    return m[v][h]


def move_on_slope(start_h, start_v, limit_h, real_h, x, y):
    # always move right x and down y
    stop_h = start_h + x
    stop_v = start_v + y
    if stop_h >= limit_h: # need to extend map
        limit_h += real_h
    return (stop_h, stop_v, limit_h)

def go_down_the_slope(m, right, down):
    # print_map(map)
    # print(max_v)
    real_max_h = len(m[0])
    max_h = real_max_h
    max_v = len(m)

    count_trees = 0

    pos_h = 0
    pos_v = 0

    while pos_v < max_v:
        
        move_result = move_on_slope(pos_h, pos_v, max_h, real_max_h, right, down)
        pos_h = move_result[0]
        pos_v = move_result[1]
        max_h = move_result[2]
        if pos_v >= max_v:
            break
        # check if it is a tree
        if check_position(pos_h, pos_v, m, real_max_h) == '#':
            count_trees += 1
        
    return count_trees

# map
# grid where the horizontal is down
# a string already behaves like a list
# the map is a list of strings
def read_map(path):
    map = list()
    with open(path) as file:
        line = file.readline()
        while line:
            map.append(line.strip())
            line = file.readline()
    return map