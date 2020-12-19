# Day 19 exercise 1
import day19

rules, messages = day19.read_input("input//input.txt")

# 8: 42 | 42 8
rule8, rule8_exp = day19.parse_rule("8: 42 +")
rules[8] = rule8_exp
# 11: 42 31 | 42 11 31
rule11, rule11_exp = day19.parse_rule("11: 42 + 31 +")
rules[11] = rule11_exp

result = day19.execute(rules, messages)

print(result)