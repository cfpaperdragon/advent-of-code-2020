# Day 14 exercise 1

def read_input(path):
    input_list = list()
    with open(path) as file:
        line = file.readline()
        while line:
            input_list.append(line.strip())
            line = file.readline()
    return input_list

def get_mask(instruction):
    return instruction[7:]

def get_values(instruction):
    simpler = instruction.replace("mem[","")
    simpler = simpler.replace("]","")
    values = simpler.split("=")
    mem_address = int(values[0].strip())
    value = int(values[1].strip())
    return mem_address, value

def make_binary(value):
    bit_list = list()
    bit_value = str(bin(value))
    i = 1
    bit_char = bit_value[-i]
    while bit_char != "b":
        bit_list.insert(0, bit_char)
        i += 1
        bit_char = bit_value[-i]
    while len(bit_list) <= 36:
        bit_list.insert(0, '0')
    return bit_list


def apply_mask(value, mask):
    bit_value = make_binary(value)
    i = 1
    new_bit_value = list()
    while i <= len(mask):
        if mask[-i] != "X":
            new_bit_value.insert(0, mask[-i])
        else:
            new_bit_value.insert(0, bit_value[-i])
        i += 1
    str_new_value = "0b" + ''.join(new_bit_value)
    return int(str_new_value, 2)


def execute(p):
    m = dict()
    mask = ""
    mem_address = 0
    value = 0
    for i in range(len(p)):
        if "mask" in p[i]:
            mask = get_mask(p[i])
            # print(mask)
        elif "mem" in p[i]:
            mem_address, value = get_values(p[i])
            m[mem_address] = apply_mask(value, mask)
            # print("mem[{}] = {}".format(mem_address, value))
    return m

program = read_input("input//input.txt")

# print(program)

memory = execute(program)
sum = 0
for key in memory.keys():
    sum += memory[key]
print(sum)
