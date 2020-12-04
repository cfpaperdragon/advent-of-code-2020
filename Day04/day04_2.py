# Day 04 exercise 2
import sys

import day04

# Add the parent folder path to the sys.path list
sys.path.append('../')

# Now you can import your module
# pylint: disable=import-error
import common


def string_passport_to_dict(pp):
    passport_data = pp.strip().split(" ")
    pp_dict = dict()
    for field in passport_data:
        splitted = field.split(":")
        pp_dict[splitted[0]] = splitted[1]
    return pp_dict

def is_valid_year(s):
    if len(s) != 4:
        False
    return common.is_int(s)

def validate_byr(byr):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if not is_valid_year(byr):
        return False
    byr_year = int(byr)
    if byr_year > 2002 or byr_year < 1920:
        return False
    return True

def validate_iyr(iyr):
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if not is_valid_year(iyr):
        return False
    iyr_year = int(iyr)
    if iyr_year > 2020 or iyr_year < 2010:
        return False
    return True

def validate_eyr(eyr):
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if not is_valid_year(eyr):
        return False
    eyr_year = int(eyr)
    if eyr_year > 2030 or eyr_year < 2020:
        return False
    return True

def validate_hgt(hgt):
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    if "in" in hgt:
        height_str = hgt.replace("in", "")
        if common.is_int(height_str):
            height = int(height_str)
            if height < 59 or height > 76:
                return False
        else:
            return False
    elif "cm" in hgt:
        height_str = hgt.replace("cm", "")
        if common.is_int(height_str):
            height = int(height_str)
            if height < 150 or height > 193:
                return False
        else:
            return False
    else:
        return False
    return True

def validate_hcl(hcl):
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if len(hcl) != 7:
        return False
    if hcl[0] != "#":
        return False
    valid_hex_chars = "0123456789abcdefABCDEF"
    for i in range(1,7):
        if hcl[i] not in valid_hex_chars:
            return False
    return True

def validate_ecl(ecl):
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if ecl not in valid_colors:
        return False
    return True

def validate_pid(pid):    
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if len(pid) != 9:
        return False
    if not common.is_int(pid):
        return False
    return True
    

def validate_passport_fields(pp_dict):
    byr_value = pp_dict["byr"]
    if not validate_byr(byr_value):
        return False

    iyr_value = pp_dict["iyr"]
    if not validate_iyr(iyr_value):
        return False

    eyr_value = pp_dict["eyr"]
    if not validate_eyr(eyr_value):
        return False

    hgt_value = pp_dict["hgt"]
    if not validate_hgt(hgt_value):
        return False

    hcl_value = pp_dict["hcl"]
    if not validate_hcl(hcl_value):
        return False

    ecl_value = pp_dict["ecl"]
    if not validate_ecl(ecl_value):
        return False

    pid_value = pp_dict["pid"]
    if not validate_pid(pid_value):
        return False

    return True
    
passports = day04.read_passports("input\\input.txt")
# print(passports)
count_valid = 0
for i in range(len(passports)):
    if day04.validate_passport(passports[i]):
        passport_in_dict = string_passport_to_dict(passports[i])
        if validate_passport_fields(passport_in_dict):
            # print("byr: {}".format(passport_in_dict["byr"]))
            # print("hgt: {}".format(passport_in_dict["hgt"]))
            count_valid += 1

print(count_valid)