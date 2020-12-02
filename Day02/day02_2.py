# Day02 exercise 2

import day02


def is_valid(pp):
    pp_password = day02.password(pp)
    pp_char = day02.policy_char(pp)
    pp_least = day02.policy_least(pp)
    pp_most = day02.policy_most(pp)
    
    return (pp_password[pp_least-1] == pp_char and not (pp_password[pp_most-1] == pp_char)) or (not (pp_password[pp_least-1] == pp_char) and pp_password[pp_most-1] == pp_char)


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