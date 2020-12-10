import re

with open('04/input.txt') as f:
    lines = f.read().splitlines()


required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def validate(fields):
    for required_field in required_fields:
        if not required_field in fields:
            return False
    return True


regex = r"([a-z]+):([a-z0-9#]+)"
valid_passports = 0
passport = {}
for line in lines:
    if len(line) == 0:
        if validate(passport):
            valid_passports += 1
        passport = {}
    else:
        matches = re.findall(regex, line)
        for match in matches:
            passport[match[0]] = match[1]
print(str(valid_passports))
