# Day 16 common

def process_field(line):
    # print(line)
    field_name = ""
    field_limits = list()
    split1 = line.split(":")
    # print(split1)
    field_name = split1[0].strip()
    split2 = split1[1].split("or")
    # print(split2)
    for limits in split2:
        # print(limits)
        split_limits = limits.strip().split("-")
        # print(split_limits)
        field_limits.append((int(split_limits[0]), int(split_limits[1])))
    return field_name, field_limits

def process_ticket(line):
    ticket_list = list()
    split1 = line.split(",")
    for value in split1:
        ticket_list.append(int(value))
    return ticket_list

def read_input(path):
    field_rules = dict()
    my_ticket = ""
    nearby_tickets = list()
    with open(path) as file:
        line = file.readline()
        while len(line.strip()) > 0:
            field_name, field_limits = process_field(line.strip())
            field_rules[field_name] = field_limits
            line = file.readline()
        line = file.readline()
        my_ticket_values = file.readline()
        my_ticket = process_ticket(my_ticket_values.strip())
        line = file.readline()
        line = file.readline()
        line = file.readline()
        while line:
            nearby_tickets.append(process_ticket(line.strip()))
            line = file.readline()
    return field_rules, my_ticket, nearby_tickets

def is_valid(value, rule_list):
    for pair in rule_list:
        if value >= pair[0] and value <= pair[1]:
            return True
    return False

def is_valid_all_rules(value, rules_dict):
    for key in rules_dict.keys():
        if is_valid(value, rules_dict[key]):
            return True
    return False

def check_valid_tickets(rules, ticket_list, cache):
    sum = 0
    for t in ticket_list:
        for value in t:
            if value not in cache.keys():
                cache[value] = is_valid_all_rules(value, rules)
            if not cache[value]:
                sum += value
    return cache, sum

