import re

with open('08/input.txt') as f:
    instructions = [[x, False] for x in f]

regex = r"([a-z]+) ([\+-][0-9]+)"
pc = 0
acc = 0
while pc < len(instructions):
    if instructions[pc][1]:
        break
    instructions[pc][1] = True
    instruction = re.match(regex, instructions[pc][0])
    if instruction[1] == "jmp":
        pc += int(instruction[2])
        continue
    elif instruction[1] == "acc":
        acc += int(instruction[2])
    pc += 1

print(str(acc))
