import re

regex = r"([0-9]+)-([0-9]+)\ ([a-z]): ([a-z]*)"
with open('02/input.txt') as f:
    matches = re.finditer(regex, f.read(), re.MULTILINE)

valid_passwords = 0
for match in matches:
    count = 0
    lower = int(match.group(1)) - 1
    upper = int(match.group(2)) - 1
    password = match.group(4)

    if len(password) > lower and password[lower] == match.group(3):
        count += 1
    if len(password) > upper and password[upper] == match.group(3):
        count += 1
    if count == 1:
        valid_passwords += 1

print(str(valid_passwords))
