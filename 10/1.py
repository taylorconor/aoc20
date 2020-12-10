with open('10/input.txt') as f:
    lines = [int(x) for x in f]
    lines.sort()

diffs = [0] * 4
diffs[lines[0]] += 1
for i in range(1, len(lines)):
    diffs[lines[i] - lines[i - 1]] += 1

print(str(diffs[1] * (diffs[3] + 1)))
