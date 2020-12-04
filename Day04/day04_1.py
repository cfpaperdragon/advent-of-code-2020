# Day 04 exercise 1

import day04    
    
passports = day04.read_passports("input\\input.txt")
# print(passports)
count_valid = 0
for i in range(len(passports)):
    if day04.validate_passport(passports[i]):
        count_valid += 1

print(count_valid)