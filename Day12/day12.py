# Day 12 common

def read_input(path):
    input_list = list()
    with open(path) as file:
        line = file.readline()
        while line:
            instruction = (line.strip()[0], int(line.strip()[1:]))
            input_list.append(instruction)
            line = file.readline()
    return input_list


def move(direction, distance, xstart, ystart, facing_direction):
    x = xstart
    y = ystart
    if direction == "N":
        # maintain x, increment y
        y += distance
    elif direction == "S":
        # maintain x, decrement y
        y -= distance
    elif direction == "E":
        # increment x, maintain y
        x += distance
    elif direction == "W":
        # decrement x, maintain y
        x -= distance
    return (x, y, facing_direction)


def rotate_internal(side, facing_direction):
    new_direction = facing_direction
    if side == "R":
        if facing_direction == "N":
            new_direction = "E"
        elif facing_direction == "E":
            new_direction = "S"
        elif facing_direction == "S":
            new_direction = "W"
        elif facing_direction == "W":
            new_direction = "N"
    elif side == "L":
        if facing_direction == "N":
            new_direction = "W"
        elif facing_direction == "W":
            new_direction = "S"
        elif facing_direction == "S":
            new_direction = "E"
        elif facing_direction == "E":
            new_direction = "N"
    return new_direction

def rotate(side, angle, xstart, ystart, facing_direction):
    # from what I've seen of the input, we are rotating multiple of 90 degree angles
    # print(angle)
    rotate_times = angle // 90
    new_direction = facing_direction
    while rotate_times > 0:
        rotate_times -= 1
        new_direction = rotate_internal(side, new_direction)
    return (xstart, ystart, new_direction)


def follow_instruction(xstart, ystart, facing_direction, instruction):
    action = instruction[0]
    result = (xstart, ystart, facing_direction)
    if action == "N":
        result = move("N", instruction[1], xstart, ystart, facing_direction)
    elif action == "S":
        result = move("S", instruction[1], xstart, ystart, facing_direction)
    elif action == "E":
        result = move("E", instruction[1], xstart, ystart, facing_direction)
    elif action == "W":
        result = move("W", instruction[1], xstart, ystart, facing_direction)
    elif action == "L":
        result = rotate("L", instruction[1], xstart, ystart, facing_direction)
    elif action == "R":
        result = rotate("R", instruction[1], xstart, ystart, facing_direction)
    elif action == "F":
        result = move(facing_direction, instruction[1], xstart, ystart, facing_direction)
    return result

def follow_all_instructions(xstart, ystart, facing_direction, instruction_list):
    x = xstart
    y = ystart
    direction = facing_direction
    for instruction in instruction_list:
        new_position = follow_instruction(x, y, direction, instruction)
        # print(new_position)
        x = new_position[0]
        y = new_position[1]
        direction = new_position[2]
    return (x, y, direction)