# Day 16 exercise 2

import day16

def is_valid_ticket(t, validation):
    for value in t:
        if not validation[value]:
            return False
    return True

def filter_valid_tickets(tickets, validation):
    valid_tickets = list()
    for t in tickets:
        if is_valid_ticket(t, validation):
            valid_tickets.append(t)
    return valid_tickets

def init_field_position_dict(fields, ticket_len):
    field_position_dict = dict()
    for i in range(ticket_len):
        field_position_dict[i] = list(fields.keys())
    return field_position_dict

def find_correct_fields(field_rules, valid_tickets, field_position_dict):
    for t in valid_tickets:
        for v in range(len(t)):
            value = t[v]
            for field in field_rules.keys():
                if field in field_position_dict[v]: # only check if it's still possible for that field position
                    if not day16.is_valid(value, field_rules[field]):
                        field_position_dict[v].remove(field)
    return field_position_dict



fields, ticket, other_tickets = day16.read_input("input//input.txt")

validation_cache, result_part1 = day16.check_valid_tickets(fields, other_tickets, dict())

valids = filter_valid_tickets(other_tickets, validation_cache)
# print(len(valids))

field_position = init_field_position_dict(fields, len(ticket))
field_position = find_correct_fields(fields, valids, field_position)

# print(field_position)

position_fields_list = list()
for key in field_position.keys():
    list_item = (key, field_position[key])
    position_fields_list.append(list_item)

position_fields_list.sort(key=lambda tup: len(tup[1]))
# print(position_fields_list)

final_ticket = dict()

while len(position_fields_list) > 0:
    first_item = position_fields_list.pop(0)
    field_name = first_item[1][0] # should only be a field on the list
    ticket_positon = first_item[0]
    final_ticket[field_name] = ticket[ticket_positon]
    # remove this name from all others where it may exist
    for position_field_pair in position_fields_list:
        if field_name in position_field_pair[1]:
            position_field_pair[1].remove(field_name)

# print(final_ticket)

accumulator = 1
for key in final_ticket.keys():
    if "departure" in key:
        accumulator *= final_ticket[key]

print(accumulator)