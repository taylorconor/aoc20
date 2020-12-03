with open('3/input.txt') as f:
    lines = f.read().splitlines()


def count_trees(right, down):
    row = 0
    col = 0
    trees = 0
    while True:
        row += down
        if row >= len(lines):
            break
        col = (col + right) % len(lines[0])
        if lines[row][col] == '#':
            trees += 1
    return trees


trees_1 = count_trees(1, 1)
trees_2 = count_trees(3, 1)
trees_3 = count_trees(5, 1)
trees_4 = count_trees(7, 1)
trees_5 = count_trees(1, 2)
print(str(trees_1 * trees_2 * trees_3 * trees_4 * trees_5))
