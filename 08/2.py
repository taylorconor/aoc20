import re

with open('08/input.txt') as f:
    data = f.read().splitlines()

regex = r"([a-z]+) ([\+-][0-9]+)"


def terminating_acc(instructions):
    pc = 0
    acc = 0
    while pc < len(instructions):
        if instructions[pc][1]:
            return 0
        instructions[pc][1] = True
        instruction = re.match(regex, instructions[pc][0])
        if instruction[1] == "jmp":
            pc += int(instruction[2])
            continue
        elif instruction[1] == "acc":
            acc += int(instruction[2])
        pc += 1
    return acc


for i in range(len(data)):
    ins = [[x, False] for x in data]
    if ins[i][0][:3] == "jmp":
        ins[i][0] = ins[i][0].replace("jmp", "nop")
    elif ins[i][0][:3] == "nop":
        ins[i][0] = ins[i][0].replace("nop", "jmp")
    acc = terminating_acc(ins)
    if acc > 0:
        print(str(acc))
        break
