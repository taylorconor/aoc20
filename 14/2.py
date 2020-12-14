import re
import itertools

with open('14/input.txt') as f:
    lines = f.readlines()

mask_regex = r"mask = ([01X]+)"
mem_regex = r"mem\[([0-9]+)\] = ([0-9]+)"
memory = {}

for line in lines:
    if match := re.search(mask_regex, line):
        zero_mask = int(match[1].replace('1', '0').replace('X', '1'), 2)
        set_mask = int(match[1].replace('X', '0'), 2)
        positions = [i for i, x in enumerate(match[1][::-1]) if x == 'X']
        offsets = set()
        for i in range(len(positions) + 1):
            for combo in itertools.combinations(positions, i):
                offsets.add(combo)
    elif match := re.search(mem_regex, line):
        for offset in offsets:
            address = (int(match[1]) & ~zero_mask) | set_mask
            for num in offset:
                address += 2 ** num
            memory[address] = int(match[2])

print(str(sum(memory.values())))
