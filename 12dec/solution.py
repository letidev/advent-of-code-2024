import time

with open("test.txt") as f:
    lines = f.read().splitlines()

n = len(lines)
m = len(lines[0])

visited = [[False for _ in range(m)] for _ in range(n)]
areas: dict[int, tuple[int, int]] = {}
cropId = 0
idx = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def getEl(i, j, n, m):
    if i < 0 or j < 0 or i >= n or j >= m:
        return ""
    else:
        return lines[i][j]


def countFences(i, j, n, m):
    return sum([1 if lines[i][j] != getEl(i+x[0], j+x[1], n, m) else 0 for x in idx])


def walk(i, j, n, m, cropId):
    if visited[i][j]:
        return

    visited[i][j] = True

    if cropId in areas:
        data = areas[cropId]
        data = (data[0] + 1, data[1] + countFences(i, j, n, m))
    else:
        data = (1, countFences(i, j, n, m))

    areas[cropId] = data

    for x in idx:
        if lines[i][j] == getEl(i+x[0], j+x[1], n, m):
            walk(i+x[0], j+x[1], n, m, cropId)


start_time = time.time()
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            walk(i, j, n, m, cropId)
            cropId += 1

total = 0
for i in range(cropId):
    total += areas[i][0] * areas[i][1]

print(time.time() - start_time, "seconds")
print(total)
