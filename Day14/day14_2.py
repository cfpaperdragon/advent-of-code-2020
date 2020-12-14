# Day 14 exercise 2

import day14

def new_apply_mask(value, mask):
    bit_value = day14.make_binary(value)
    i = 1
    new_bit_value = list()
    while i <= len(mask):
        if mask[-i] == "1":
            new_bit_value.insert(0, "1")
        elif mask[-i] == "0":
            new_bit_value.insert(0, bit_value[-i])
        else: # "X"
            new_bit_value.insert(0, "X")
        i += 1
    str_new_value = ''.join(new_bit_value)
    return str_new_value

def unfold_address(address):
    i = 1
    unfold_address = address
    address_list = list()
    while i <= len(unfold_address):
        if unfold_address[-i] == "X":
            address_len = len(unfold_address)
            if i == address_len:
                unfold_address_0 = "0" + unfold_address[-i+1:]
                unfold_address_1 = "1" + unfold_address[-i+1:]
            elif i == 1:
                unfold_address_0 = unfold_address[:-i] + "0"
                unfold_address_1 = unfold_address[:-i] + "1"
            else:
                unfold_address_0 = unfold_address[:-i] + "0" + unfold_address[-i+1:]
                unfold_address_1 = unfold_address[:-i] + "1" + unfold_address[-i+1:]
            address_list.append(unfold_address_0)
            address_list.append(unfold_address_1)
            break
        i += 1
    return address_list

def unfold_all_addresses(address_list):
    new_list = list()
    while "X" in address_list[0]:
        while len(address_list) > 0:
            address = address_list.pop(0)
            unfolded_list = unfold_address(address)
            for unfolded in unfolded_list:
                new_list.append(unfolded)
        address_list = new_list
    return new_list

def new_execute(p):
    m = dict()
    mask = ""
    mem_address = 0
    value = 0
    for i in range(len(p)):
        if "mask" in p[i]:
            mask = day14.get_mask(p[i])
            # print(mask)
        elif "mem" in p[i]:
            print("mem[{}] = {}".format(mem_address, value))
            mem_address, value = day14.get_values(p[i])
            address_template = new_apply_mask(mem_address, mask)
            address_list = list()
            address_list.append(address_template)
            address_list = unfold_all_addresses(address_list)
            print(address_list)           
    return m

program = day14.read_input("input//example02.txt")

# print(program)

memory = new_execute(program)
# sum = 0
# for key in memory.keys():
#     sum += memory[key]
# print(sum)