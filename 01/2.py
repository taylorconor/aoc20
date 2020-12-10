with open('01/input.txt') as f:
    inputs = [int(x) for x in f]

for first_input in inputs:
    first_diff = 2020 - first_input
    for second_input in inputs:
        second_diff = first_diff - second_input
        if second_diff in inputs:
            print(str(first_input * second_input * second_diff)))
            exit()
