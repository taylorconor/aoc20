with open('13/input.txt') as f:
    l = f.readlines()
    busses = [(int(x), i) for i, x in enumerate(l[1].split(",")) if x != "x"]

product = busses[0][0]
busses.pop(0)
idx = 0
while len(busses) > 0:
    idx += product
    to_remove = set()
    for i, bus in enumerate(busses):
        if (idx + bus[1]) % bus[0] == 0:
            product *= bus[0]
            to_remove.add(i)
    if len(to_remove) > 0:
        busses = [x for i, x in enumerate(busses) if i not in to_remove]
print(str(idx))
