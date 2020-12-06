with open('6/input.txt') as f:
    data = f.read()

tot = 0
ids = set()
for line in data.splitlines():
    if len(line) == 0:
        tot += len(ids)
        ids = set()
        continue
    for c in line:
        ids.add(c)
tot += len(ids)

print(str(tot))
