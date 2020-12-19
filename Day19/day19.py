# Day 19 common
import sys
import re

# Add the parent folder path to the sys.path list
sys.path.append('../')

# Now you can import your module
# pylint: disable=import-error
import common

def parse_rule(expression):
    split_colon = expression.split(":")
    rule_number = int(split_colon[0])
    rule_expression = split_colon[1].strip()
    if "\"" in rule_expression:
        rule_expression = rule_expression.replace("\"", "")
        return rule_number, rule_expression
    else:
        tokens = rule_expression.split(" ")
        final_list = list()
        for token in tokens:
            if common.is_int(token):
                final_list.append(int(token))
            else:
                final_list.append(token)
        return rule_number, final_list

def read_input(path):
    with open(path) as file:
        rules_dict = dict()
        line = file.readline()
        while len(line.strip()) > 0:
            rule_number, rule_expression = parse_rule(line.strip())
            rules_dict[rule_number] = rule_expression
            line = file.readline()
        
        message_list = list()
        line = file.readline()
        while line:
            message_list.append(line.strip())
            line = file.readline()
    return rules_dict, message_list

def replace_in_rules(rules_dict, rule_key):
    value = rules_dict[rule_key]
    if type(value) is not list:
        for key in rules_dict.keys():
            if type(rules_dict[key]) is list:
                while rule_key in rules_dict[key]:
                    index = rules_dict[key].index(rule_key)
                    rules_dict[key][index] = value
    else:
        # surround with parentesis
        value.append(")")
        value.insert(0, "(")
        for key in rules_dict.keys():
            if type(rules_dict[key]) is list:
                while rule_key in rules_dict[key]:
                    index = rules_dict[key].index(rule_key)
                    if index == 0:
                        rules_dict[key] = value + rules_dict[key][index+1:]
                    elif index == len(rules_dict[key])-1:
                        rules_dict[key] = rules_dict[key][:index] + value
                    else:
                    #     print(rules_dict[key])
                    #     print(rules_dict[key][:index])
                    #     print(rules_dict[key][index+1:])
                        rules_dict[key] = rules_dict[key][:index] + value + rules_dict[key][index+1:]
                    # print(rules_dict[key])

def check_numbers(l):
    for item in l:
        if type(item) is int:
            return True
    return False

def execute(rules, messages):
    cleared = list()
    while check_numbers(rules[0]):
        rules_without_numbers = list()
        for key in rules.keys():
            if key in cleared:
                continue
            else:
                if type(rules[key]) is not list:
                    rules_without_numbers.append(key)
                elif check_numbers(rules[key]):
                    rules_without_numbers.append(key)

        for key in rules_without_numbers:
            replace_in_rules(rules, key)
            cleared.append(key)

    exp = "".join(rules[0])
    exp = exp.replace("X", "5")
    # print(exp)
    p = re.compile("^" + exp + "$")

    count = 0
    for message in messages:
        m = p.match(message)
        if m:
            count += 1
    return count
