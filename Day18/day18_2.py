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
    tokens = e.split(" ")
    token_list = list(tokens)
    return resolve_in_place_tokens(token_list, 0, len(token_list))

def resolve_in_place_tokens(token_list, start, end):
    while "+" in token_list:
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
    print(token_list)
        

expression_list = day18.read_input("input//example.txt")

resolve_in_place(expression_list[0])
