nums = [0, 8, 15, 2, 12, 1, 4]
spoken = {}
current = -1
for i, num in enumerate(nums):
    spoken[current] = i
    current = num
for i in range(len(nums), 30000000):
    if current in spoken:
        prev = spoken[current]
        spoken[current] = i
        current = i - prev
    else:
        spoken[current] = i
        current = 0
print(str(current))
