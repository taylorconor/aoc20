from copy import deepcopy

with open('11/input.txt') as f:
    grid = [list(x) for x in f]


neighbours = [(-1, -1), (0, -1), (1, -1), (-1, 0),
              (1, 0), (-1, 1), (0, 1), (1, 1)]


def count_occupied(i, j, grid):
    tot = 0
    for pos in neighbours:
        p_i, p_j = i + pos[1], j + pos[0]
        if p_i < 0 or p_i >= len(grid) or p_j < 0 or p_j >= len(grid[0]):
            continue
        if grid[p_i][p_j] == "#":
            tot += 1
    return tot


def apply_rules(grid):
    new_grid = deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                continue
            occupied = count_occupied(i, j, grid)
            if grid[i][j] == "L" and occupied == 0:
                new_grid[i][j] = "#"
            elif grid[i][j] == "#" and occupied >= 4:
                new_grid[i][j] = "L"
    return new_grid


new_grid = apply_rules(grid)
while grid != new_grid:
    grid = new_grid
    new_grid = apply_rules(grid)

tot = 0
for line in grid:
    tot += line.count("#")
print(str(tot))
