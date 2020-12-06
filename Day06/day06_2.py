# Day 06 exercise 2

def read_answers(path):
    group_list = list()
    with open(path) as file:
        line = file.readline()
        answers = list()
        while line:
            if len(line.strip()) == 0:
                group_list.append(answers)
                answers = list()
            else:
                answers.append(line.strip())
            line = file.readline()
        # add last one
        group_list.append(answers)

    return group_list

def count_group(g):
    questions = "abcdefghijklmnopqrstuxyvwz"

    count_answers = dict()
    for question in questions:
        count = 0
        for answer_list in g:
            if question in answer_list:
                count += 1
        count_answers[question] = count
    
    number_lists = len(g)
    count_all_answers = 0
    for key in count_answers:
        if count_answers[key] == number_lists:
            count_all_answers += 1

    return count_all_answers

groups = read_answers("input\\input.txt")

total = 0
for group in groups:
    # print(group)
    result = count_group(group)
    total += result

print(total)
