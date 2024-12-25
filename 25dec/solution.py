import time

with open("test.txt") as f:
    lines = f.read().split("\n\n")

lines = [line.splitlines() for line in lines]

n = len(lines[0])
m = len(lines[0][0])
maxh = n - 2

locks = []
keys = []

start_time = time.time()
for item in lines:
    pins = [-1 for _ in range(m)]

    is_lock = True if item[0].startswith("#") else False

    for i in range(n):
        for j in range(m):
            if item[i][j] == "#":
                pins[j] += 1

    if is_lock:
        locks.append(pins)
    else:
        keys.append(pins)


pairs = 0
for lock in locks:
    for key in keys:
        if max([lock[i]+key[i] for i in range(m)]) <= maxh:
            pairs += 1

print(pairs)
print(time.time() - start_time, "seconds")
