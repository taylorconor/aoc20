with open('09/input.txt') as f:
    lines = [int(x) for x in f]

target = 1124361034
start = 0
end = 0
tot = lines[0] + lines[1]
for end in range(2, len(lines)):
    if tot == target:
        break
    tot += lines[end]
    while tot > target and (end - start) > 0:
        tot -= lines[start]
        start += 1


subset = lines[start:end]
subset.sort()
print(str(subset[0] + subset[-1]))
