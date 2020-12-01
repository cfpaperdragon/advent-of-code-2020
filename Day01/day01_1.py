# Day01 exercise 1

expense_report = list()

with open("input\\input.txt") as file:
    line = file.readline()
    count = 1
    while line:
        # print("Line {}: {}".format(count, line.strip()))
        value = int(line.strip())
        expense_report.append(value)
        line = file.readline()
        count += 1

for i in range(len(expense_report)):
    for j in range(i+1,len(expense_report)):
        if expense_report[i] + expense_report[j] == 2020:
             print("i={}, j={}, result={}".format(i, j, expense_report[i]*expense_report[j]))
             break

