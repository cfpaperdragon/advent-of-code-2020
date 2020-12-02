# Day02 exercise 1

import day02


def is_valid(pp):
    pp_password = day02.password(pp)
    pp_char = day02.policy_char(pp)
    pp_least = day02.policy_least(pp)
    pp_most = day02.policy_most(pp)
    count_char = 0
    for i in range(len(pp_password)):
        if pp_password[i] == pp_char:
            count_char += 1
    return pp_least <= count_char and count_char <= pp_most


with open("input\\input.txt") as file:
    line = file.readline()
    count = 1
    count_valid = 0
    while line:
        policy_password = day02.parse_policy_password(line)
        if len(policy_password) > 4:
            print(policy_password)
            break
        else:
            if is_valid(policy_password):
                count_valid += 1

        line = file.readline()
        count += 1

print(count_valid)