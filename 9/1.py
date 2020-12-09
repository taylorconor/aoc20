with open('9/input.txt') as f:
    lines = [int(x) for x in f]

window = []
for i in range(len(lines)):
    if i > 24:
        exists = False
        for j in range(i - 25, i):
            if lines[i] in window[j]:
                exists = True
                break
        if not exists:
            print(lines[i])
            break
    window.append(set())
    for j in range(max(i - 25, 0), i):
        window[j].add(lines[i] + lines[j])
