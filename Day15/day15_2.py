# Day 15 exercise 1

def read_input(path):
    with open(path) as file:
        line = file.readline()
        input_list = list()
        inputs = line.strip().split(",")
        # print(inputs)
        for number in inputs:
            input_list.append(int(number))
    return input_list

def do_turn(last_number, last_turn, cache_dict):
    # print("last_number={}, last_turn={}".format(last_number, last_turn))
    # print(cache_dict)
    next_number = 0
    if last_number in cache_dict.keys():
        if len(cache_dict[last_number]) == 1: # Is First Time?
            next_number = 0
        else:
            next_number = last_turn - cache_dict[last_number][-2]
    if next_number in cache_dict.keys():
        cache_dict[next_number].append(last_turn + 1)
        if len(cache_dict[next_number]) > 2:
            cache_dict[next_number] = cache_dict[next_number][-2:]
    else:
        cache_dict[next_number] = list()
        cache_dict[next_number].append(last_turn + 1)
    return next_number

def elf_game(starting_list, stop_turn, cache_dict):
    turn_counter = 0
    last_number = 0
    for number in starting_list:
        turn_counter += 1
        last_number = number
        cache_dict[number] = list()
        cache_dict[number].append(turn_counter)
        

    while turn_counter < stop_turn:
        last_number = do_turn(last_number, turn_counter, cache_dict)
        turn_counter += 1
        # print("turn_counter:{}, last_number:{}".format(turn_counter, last_number))
    
    return last_number
    

starting_numbers = read_input("input//input.txt")
    
cache = dict() # save two things number = list of times it appeared

result = elf_game(starting_numbers, 30000000, cache)
# print(cache)
print(result)