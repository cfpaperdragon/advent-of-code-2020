# Day 12 exercise 2

import day12

def internal_rotate_waypoint(side, x_pos, y_pos):
    x = 0
    y = 0
    if side == "R":
        x = y_pos
        y = x_pos * (-1)
    elif side == "L":
        x = y_pos * (-1)
        y = x_pos
    return (x, y)

def rotate_waypoint(side, angle, x_pos, y_pos):
    # the waypoint rotates in turn of ship which we can assume is always on 0,0
    x = x_pos
    y = y_pos
    rotation_times = angle // 90
    while rotation_times > 0:
        rotation_times -= 1
        result = internal_rotate_waypoint(side, x, y)
        x = result[0]
        y = result[1]
    return (x, y)

def move_waypoint_direction(distance, x_ship, y_ship, x_wp, y_wp):
    x = x_ship + x_wp * distance
    y = y_ship + y_wp * distance
    return (x, y)

def new_follow_instruction(x_ship, y_ship, x_wp, y_wp, instruction):
    action = instruction[0]
    return_result = ()
    if action == "N":
        # move waypoint north
        result = day12.move("N", instruction[1], x_wp, y_wp, "")
        return_result = (x_ship, y_ship, result[0], result[1])
    elif action == "S":
        result = day12.move("S", instruction[1], x_wp, y_wp, "")
        return_result = (x_ship, y_ship, result[0], result[1])
    elif action == "E":
        result = day12.move("E", instruction[1], x_wp, y_wp, "")
        return_result = (x_ship, y_ship, result[0], result[1])
    elif action == "W":
        result = day12.move("W", instruction[1], x_wp, y_wp, "")
        return_result = (x_ship, y_ship, result[0], result[1])
    elif action == "R":
        result = rotate_waypoint("R", instruction[1], x_wp, y_wp)
        return_result = (x_ship, y_ship, result[0], result[1])
    elif action == "L":
        result = rotate_waypoint("L", instruction[1], x_wp, y_wp)
        return_result = (x_ship, y_ship, result[0], result[1])
    elif action == "F":
        result = move_waypoint_direction(instruction[1], x_ship, y_ship, x_wp, y_wp)
        return_result = (result[0], result[1], x_wp, y_wp)
    return return_result

def new_follow_all_instructions(x_ship, y_ship, x_wp, y_wp, instruction_list):
    x = x_ship
    y = y_ship
    xx = x_wp
    yy = y_wp
    for instruction in instruction_list:
        new_position = new_follow_instruction(x, y, xx, yy, instruction)
        # print(new_position)
        x = new_position[0]
        y = new_position[1]
        xx = new_position[2]
        yy = new_position[3]
    return (x, y)

instructions = day12.read_input("input//input.txt")
# print(instructions)

ship_start_x = 0
ship_start_y = 0

# waypoint is always relative to the ship
waypoint_start_x = 10
waypoint_start_y = 1

result = new_follow_all_instructions(ship_start_x, ship_start_y, waypoint_start_x, waypoint_start_y, instructions)

print(result)
print(abs(result[0])+abs(result[1]))
