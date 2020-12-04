# Day 04 exercise 2

import day04

# https://stackoverflow.com/questions/1265665/how-can-i-check-if-a-string-represents-an-int-without-using-try-except
def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

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
    return is_int(s)

def validate_byr(byr):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if not is_valid_year(byr):
        return False
    byr_year = int(byr)
    if byr_year > 2002 or byr_year < 1920:
        return False
    return True

def validate_passport_fields(pp_dict):
    byr_value = pp_dict["byr"]
    if not validate_byr(byr_value):
        return False

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    iyr = pp_dict["iyr"]
    if not is_valid_year(iyr):
        return False
    iyr_year = int(iyr)
    if iyr_year > 2020 or iyr_year < 2010:
        return False

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    eyr = pp_dict["eyr"]
    if not is_valid_year(eyr):
        return False
    eyr_year = int(eyr)
    if eyr_year > 2030 or eyr_year < 2020:
        return False

    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    hgt = pp_dict["hgt"]
    if "in" in hgt:
        height_str = hgt.replace("in", "")
        if is_int(height_str):
            height = int(height_str)
            if height < 59 or height > 76:
                return False
        else:
            return False
    elif "cm" in hgt:
        height_str = hgt.replace("cm", "")
        if is_int(height_str):
            height = int(height_str)
            if height < 150 or height > 193:
                return False
        else:
            return False
    else:
        return False

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    hcl = pp_dict["hcl"]
    if len(hcl) != 7:
        return False
    if hcl[0] != "#":
        return False
    valid_hex_chars = "0123456789abcdefABCDEF"
    for i in range(1,7):
        if hcl[i] not in valid_hex_chars:
            return False

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    ecl = pp_dict["ecl"]
    valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if ecl not in valid_colors:
        return False
    
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    pid = pp_dict["pid"]
    if len(pid) != 9:
        return False
    if not is_int(pid):
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