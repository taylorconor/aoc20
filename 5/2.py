with open('5/input.txt') as f:
    lines = f.read().splitlines()

ids = set()
for line in lines:
    row = int(line[:-3].replace('F', '0').replace('B', '1'), 2)
    col = int(line[-3:].replace('L', '0').replace('R', '1'), 2)
    ids.add((row * 8) + col)

for seat_id in ids:
    if (seat_id + 1) not in ids and (seat_id + 2) in ids:
        print(str(seat_id + 1))
