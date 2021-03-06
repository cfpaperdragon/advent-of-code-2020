# Day 06 exercise 1

def read_answers(path):
    group_list = list()
    with open(path) as file:
        line = file.readline()
        answers = ""
        while line:
            if len(line.strip()) == 0:
                # line break between passports
                answers = answers.replace("\n", " ")
                group_list.append(answers)
                answers = ""
            else:
                answers += line
            line = file.readline()
        # add last one
        answers = answers.replace("\n", " ")
        group_list.append(answers)

    return group_list

def count_group(g):
    questions = "abcdefghijklmnopqrstuxyvwz"

    count_answers = 0
    for question in questions:
        if question in g:
            count_answers += 1

    return count_answers

groups = read_answers("input\\input.txt")
# print(groups)

total = 0
for group in groups:
    result = count_group(group)
    total += result

print(total)
