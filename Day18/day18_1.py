# Day 18 exercise 1

import day18
import sys
# Add the parent folder path to the sys.path list
sys.path.append('../')

# Now you can import your module
# pylint: disable=import-error
import common



def parse_expression(expression):
    result = 0
    e = expression
    # print(e)
    last_token = ""
    while len(e) > 0:
        splitted = e.split(" ")
        # print(splitted)
        first_token = splitted[0]
        # token is a number
        if common.is_int(first_token):
            value = int(first_token)
            if result == 0:
                result = value
            else:
                if last_token == "+":
                    result += value
                elif last_token == "*":
                    result *= value
                else:
                    print("something is wrong: last_token:{}, value:{}".format(last_token, value))
                    return result
        elif first_token == "+" or first_token == "*":
            last_token = first_token
        elif "(" in first_token:
            # start parse of sub expression
            sub_value, remaining_expression = parse_expression(e[1:])
            if result == 0:
                result = sub_value
            else:
                if last_token == "+":
                    result += sub_value
                elif last_token == "*":
                    result *= sub_value
                else:
                    print("something is wrong: last_token:{}, sub_value:{}".format(last_token, sub_value))
                    return result, ""
            # print("sub query result:{}".format(sub_value))
            e = remaining_expression
            continue
        elif ")" in first_token:
            # end parse of sub expression
            no_parentesis = first_token
            while ")" in no_parentesis:
                no_parentesis = no_parentesis.replace(")", "")
            if common.is_int(no_parentesis):
                value = int(no_parentesis)
                if result == 0:
                    result = value
                else:
                    if last_token == "+":
                        result += value
                    elif last_token == "*":
                        result *= value
                    else:
                        print("something is wrong: last_token:{}, value:{}".format(last_token, value))
                        return result, ""
            # only want to advance the first )
            return result, e[first_token.index(")")+1:]
        # else:
            # print("unknown token:{}".format(first_token))
        e = e[len(first_token)+1:]
    return result, ""


expression_list = day18.read_input("input//input.txt")

total = 0
for exp in expression_list:
    expression_value = parse_expression(exp)
    total += expression_value[0]
print(total)
