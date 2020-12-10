with open('05/input.txt') as f:
    lines = f.read().splitlines()

max_seat_id = 0
for line in lines:
    row = int(line[:-3].replace('F', '0').replace('B', '1'), 2)
    col = int(line[-3:].replace('L', '0').replace('R', '1'), 2)
    seat_id = (row * 8) + col
    if seat_id > max_seat_id:
        max_seat_id = seat_id

print(str(max_seat_id))
