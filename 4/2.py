import re

with open('4/input.txt') as f:
    lines = f.read().splitlines()


required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
required_eyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def validate(fields):
    for required_field in required_fields:
        if not required_field in fields:
            return False
    try:
        byr = int(fields["byr"])
        if byr < 1920 or byr > 2002:
            return False
        iyr = int(fields["iyr"])
        if iyr < 2010 or iyr > 2020:
            return False
        eyr = int(fields["eyr"])
        if eyr < 2020 or eyr > 2030:
            return False
        hgt = str(fields["hgt"])
        if hgt.endswith("cm") and len(hgt) == 5:
            cm = int(hgt[:-2])
            if cm < 150 or cm > 193:
                return False
        elif hgt.endswith("in") and len(hgt) == 4:
            inch = int(hgt[:-2])
            if inch < 59 or inch > 76:
                return False
        else:
            return False
        hcl = str(fields["hcl"])
        if hcl[0] != "#" or len(hcl) != 7:
            return False
        if fields["ecl"] not in required_eyes:
            return False
        if len(str(fields["pid"])) != 9:
            return False
    except ValueError:
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
