import time

with open("test.txt") as f:
    lines = f.read().splitlines()

n = len(lines)
m = len(lines[0])

visited = [[False for _ in range(m)] for _ in range(n)]
areas: dict[int, tuple[int, int, int]] = {}
cropId = 0

IDX = [(1, 0), (-1, 0), (0, 1), (0, -1)]
EDGE_CAPS = [
    [(-1, 0), (-1, -1), (0, -1)],  # Top Left
    [(0, -1), (1, -1), (1, 0)],  # Top Right
    [(1, 0), (1, 1), (0, 1)],  # Bottom Right
    [(0, 1), (-1, 1), (-1, 0)],  # Bottom Left
]


def getEl(i, j, n, m):
    if i < 0 or j < 0 or i >= n or j >= m:
        return ""
    else:
        return lines[i][j]


def countFences(i, j, n, m):
    return sum([1 if lines[i][j] != getEl(i+x[0], j+x[1], n, m) else 0 for x in IDX])


def countCorners(i, j, n, m):
    corners = 0
    for cap in EDGE_CAPS:
        inside = sum([1 if lines[i][j] == getEl(
            i+x[0], j+x[1], n, m) else 0 for x in cap])
        corner_inside = lines[i][j] == getEl(i+cap[1][0], j+cap[1][1], n, m)

        # 1. external corner
        # 2. external corner pointing to external corner of the same area diagonally
        # 3. internal corner
        if inside == 0 or (inside == 1 and corner_inside) or (inside == 2 and not corner_inside):
            corners += 1

    return corners


def walk(i, j, n, m, cropId):
    if visited[i][j]:
        return

    visited[i][j] = True

    if cropId in areas:
        data = areas[cropId]
        data = (data[0] + 1, data[1] + countFences(i, j, n, m),
                data[2] + countCorners(i, j, n, m))
    else:
        data = (1, countFences(i, j, n, m), countCorners(i, j, n, m))

    areas[cropId] = data

    for x in IDX:
        if lines[i][j] == getEl(i+x[0], j+x[1], n, m):
            walk(i+x[0], j+x[1], n, m, cropId)


start_time = time.time()
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            walk(i, j, n, m, cropId)
            cropId += 1

total1 = 0
total2 = 0
for i in range(cropId):
    total1 += areas[i][0] * areas[i][1]
    total2 += areas[i][0] * areas[i][2]

print(time.time() - start_time, "seconds")
print("Part 1", total1)
print("Part 2", total2)
