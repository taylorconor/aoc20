import re

regex = r"([0-9]+)-([0-9]+)\ ([a-z]): ([a-z]*)"
with open('02/input.txt') as f:
    matches = re.finditer(regex, f.read(), re.MULTILINE)

valid_passwords = 0
for match in matches:
    count = 0
    for char in match.group(4):
        if char == match.group(3):
            count += 1
    if count >= int(match.group(1)) and count <= int(match.group(2)):
        valid_passwords += 1

print(str(valid_passwords))
