with open('6/input.txt') as f:
    lines = f.read().splitlines()

tot = 0
group = set()
new_group = True
for line in lines:
    if len(line) == 0:
        tot += len(group)
        group = set()
        new_group = True
        continue
    ids = set()
    for c in line:
        ids.add(c)
    if new_group:
        group = ids
        new_group = False
    else:
        group = group.intersection(ids)
tot += len(group)

print(str(tot))
