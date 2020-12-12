with open('12/input.txt') as f:
    lines = f.readlines()

x = 0
y = 0
d = 1
directions = ["N", "E", "S", "W"]
for line in lines:
    cmd = line[0]
    amt = int(line[1:])
    if cmd == "F":
        cmd = directions[d]
    if cmd == "N":
        y += amt
    elif cmd == "S":
        y -= amt
    elif cmd == 'E':
        x += amt
    elif cmd == "W":
        x -= amt
    else:
        if cmd == "L":
            amt *= -1
        d = (d + int(amt/90)) % 4

print(str(abs(x) + abs(y)))
