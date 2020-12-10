with open('03/input.txt') as f:
    lines = f.read().splitlines()

row = 0
col = 0
trees = 0
while row < len(lines) - 1:
    row += 1
    col = (col + 3) % len(lines[0])
    if lines[row][col] == '#':
        trees += 1
print(str(trees))
