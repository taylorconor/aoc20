with open('13/input.txt') as f:
    lines = f.readlines()

earliest_departure = int(lines[0])
busses = [int(x) for x in lines[1].split(",") if x != "x"]
bus_taken = busses[0]
min_wait = busses[0]

for bus in busses:
    wait = bus - earliest_departure % bus
    if wait < min_wait:
        min_wait = wait
        bus_taken = bus
print(str(bus_taken * min_wait))
