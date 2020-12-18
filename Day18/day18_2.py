# Day 18 exercise 2

import day18
import sys
# Add the parent folder path to the sys.path list
sys.path.append('../')

# Now you can import your module
# pylint: disable=import-error
import common

# idea: make a tree instead of using stack like parser

def make_tree(tokens):
    if len(tokens) == 1:
        return tokens[0]
    left = tokens.pop(0)
    operation = tokens.pop(0)
    right = make_tree(tokens)
    return (left, operation, right)

def make_expression_tree(expression):
    # prepare expression
    e = expression.replace("(", " ( ")
    e = e.replace(")", " ) ")
    print(e)
    tokens = e.split(" ")
    token_list = list(tokens)
    print(token_list)
    my_tree = make_tree(token_list)
    return my_tree


expression_list = day18.read_input("input//example.txt")

tree = make_expression_tree(expression_list[0])
print(tree)
