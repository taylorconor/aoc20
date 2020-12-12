with open('12/input.txt') as f:
    lines = f.readlines()

s_x = 0
s_y = 0
w_x = 10
w_y = 1
for line in lines:
    cmd = line[0]
    amt = int(line[1:])
    if cmd == "F":
        s_x, s_y = s_x + w_x * amt, s_y + w_y * amt
    elif cmd == "N":
        w_y += amt
    elif cmd == "S":
        w_y -= amt
    elif cmd == 'E':
        w_x += amt
    elif cmd == "W":
        w_x -= amt
    else:
        if cmd == "L":
            amt *= -1
        d = int(amt/90) % 4
        if d == 1:
            w_x, w_y = w_y, -w_x
        elif d == 2:
            w_x, w_y = -w_x, -w_y
        elif d == 3:
            w_x, w_y = -w_y, w_x

print(str(abs(s_x) + abs(s_y)))
