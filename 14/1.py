import re

with open('14/input.txt') as f:
    lines = f.readlines()

mask_regex = r"mask = ([01X]+)"
mem_regex = r"mem\[([0-9]+)\] = ([0-9]+)"
memory = {}

for line in lines:
    if match := re.search(mask_regex, line):
        zero_mask = int(match[1].replace('X', '1'), 2)
        set_mask = int(match[1].replace('X', '0'), 2)
    elif match := re.search(mem_regex, line):
        val = (int(match[2]) & zero_mask) | set_mask
        memory[int(match[1])] = val

print(str(sum(memory.values())))
