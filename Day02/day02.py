# Day02 common

# 1-3 a: abcde
# (1 3 "a" "abcde")

def policy_least(pp):
    return pp[0]

def policy_most(pp):
    return pp[1]

def policy_char(pp):
    return pp[2]

def password(pp):
    return pp[3]

def parse_policy_password(text):
    first_item = 0
    second_item = 0
    third_item = ""
    fourth_item = ""
    
    step1 = text.strip().split(" ")
    if len(step1) != 3:
        return "error: incorrect split by space"
    else: 
        fourth_item = step1[2]

    step2 = step1[0].split("-")
    if len(step2) != 2:
        return "error: incorrect split by hiffen"
    else:
        first_item = int(step2[0])
        second_item = int(step2[1])

    third_item = step1[1][0]

    return (first_item, second_item, third_item, fourth_item)
