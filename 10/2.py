import functools

with open('10/input.txt') as f:
    lines = [int(x) for x in f]
    lines.sort()
    lines.append(lines[-1] + 3)


@functools.lru_cache(maxsize=128)
def find_distinct(start_idx, prev_val):
    tot = 0
    for i in range(start_idx, len(lines)):
        if lines[i] - prev_val in range(1, 4):
            if i == len(lines) - 1:
                return 1
            tot += find_distinct(i + 1, lines[i])
        else:
            break
    return tot


print(str(find_distinct(0, 0)))
