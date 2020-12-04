# Day 04 common

def read_passports(path):
    passport_list = list()
    with open(path) as file:
        line = file.readline()
        passport = ""
        while line:
            if len(line.strip()) == 0:
                # line break between passports
                passport = passport.replace("\n", " ")
                passport_list.append(passport)
                passport = ""
            else:
                passport += line
            line = file.readline()
        # add last one
        passport = passport.replace("\n", " ")
        passport_list.append(passport)

    return passport_list

def validate_passport(pp):
    passport_data = pp.strip().split(" ")
    if len(passport_data) < 7:
        return False

    mandatory_data = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in mandatory_data:
        if field not in pp:
            return False

    return True
