# Day 18 exercise 2

import day18
import sys
# Add the parent folder path to the sys.path list
sys.path.append('../')

# Now you can import your module
# pylint: disable=import-error
import common

# idea put parentesis around + operations then use last exercise parser
# other idea: calculate the + first in the token list
# start by processing the parentesis
# start by the last ( that should match the closest )

def resolve_in_place(expression):
    # prepare expression
    e = expression.replace("(", " ( ")
    e = e.replace(")", " ) ")
    # print(e)
    tokens = e.strip().split(" ")
    token_list = list()
    for token in tokens:
        if len(token.strip()) == 0:
            continue
        token_list.append(token.strip())
    return resolve_in_place_tokens(token_list)

def last_index_of(token_list, token):
    # print(token_list)
    if "(" in token_list:
        index = token_list.index("(")
        last_index = index
        while index >= 0:
            # print(last_index)
            last_index = index
            if "(" in token_list[index+1:]:
                index = token_list.index("(", last_index+1)
            else:
                break 
        return last_index
    else:
        return -1
            
def resolve_in_place_tokens(token_list):
    while "(" in token_list:
        # print(token_list)
        index_open = last_index_of(token_list, "(")
        index_close = token_list.index(")", index_open)
        parentesis_value = resolve_in_place_tokens(token_list[index_open+1:index_close])[0]
        for i in range(index_close,index_open, -1):
            # print(i)
            del token_list[i]
        token_list[index_open] = parentesis_value
    while "+" in token_list:
        # print(token_list)
        index = token_list.index("+")
        value_before = 0
        value_after = 0
        if token_list[index-1] != ")":
            value_before = int(token_list[index-1])
        else:
            value_before = 0
        if token_list[index+1] != "(":
            value_after = int(token_list[index+1])
        else:
            value_after = 0
        total = value_before + value_after
        # replace the first value, remove the others
        token_list[index-1] = total
        del token_list[index]
        del token_list[index]
    while "*" in token_list:
        index = token_list.index("*")
        value_before = 0
        value_after = 0
        if token_list[index-1] != ")":
            value_before = int(token_list[index-1])
        else:
            value_before = 0
        if token_list[index+1] != "(":
            value_after = int(token_list[index+1])
        else:
            value_after = 0
        total = value_before * value_after
        # replace the first value, remove the others
        token_list[index-1] = total
        del token_list[index]
        del token_list[index]
    return token_list
        

expression_list = day18.read_input("input//input.txt")

# result = resolve_in_place(expression_list[0])
# print(result)

total = 0
for exp in expression_list:
    expression_value = resolve_in_place(exp)
    total += expression_value[0]
print(total)
