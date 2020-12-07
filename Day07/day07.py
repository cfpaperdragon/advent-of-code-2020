# Day 07 common

def parse_line(l):
    contain_split = l.strip().split("contain")
    outside_bag = contain_split[0].replace("bags","").strip()
    inside_bags = contain_split[1].strip()
    if inside_bags == "no other bags.":
        return (outside_bag, list())
    else:
        comma_split = inside_bags.split(",")
        inside_bag_list = list()
        for item in comma_split:
            final_bag = item.replace("bags.", "")
            final_bag = final_bag.replace("bag.", "")
            final_bag = final_bag.replace("bags", "")
            final_bag = final_bag.replace("bag", "")
            final_bag = final_bag.strip()
            space_index = final_bag.index(" ")
            how_many = int(final_bag[0:space_index])
            color = final_bag[space_index+1:]
            result = (how_many, color)
            inside_bag_list.append(result)
    return (outside_bag, inside_bag_list)

def read_dictionaries(path):
    contains_dict = dict()
    is_contained_dict = dict()
    with open(path) as file:
        line = file.readline()
        while line:
            # print(line)
            parsed_line = parse_line(line)
            # print(parsed_line)
            contains_dict[parsed_line[0]] = parsed_line[1]
            for pairing in parsed_line[1]:
                color_of_pairing = pairing[1]
                if color_of_pairing in is_contained_dict:
                    is_contained_dict[color_of_pairing].append(parsed_line[0])
                else:
                    new_list = list()
                    new_list.append(parsed_line[0])
                    is_contained_dict[color_of_pairing] = new_list
            line = file.readline()
    return contains_dict, is_contained_dict

def pretty_print_dict(name, d):
    print(name)
    for key in d:
        print("{}:{}".format(key, d[key]))