with open('01/input.txt') as f:
    inputs = [int(x) for x in f]

for input in inputs:
    diff = 2020 - input
    if diff in inputs:
        print(str(input * diff))
        exit()
