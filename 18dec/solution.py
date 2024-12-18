import time
from heapq import heappop, heappush

with open("test.txt") as f:
    lines = f.read().splitlines()

type = "test"
n = 7 if type == "example" else 71
fallen_bytes = 12 if type == "example" else 1024

dirmap = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # up, left, down, right
maze = [["." for _ in range(n)] for _ in range(n)]


def walk(n):
    visited = [[float('inf') for _ in range(n)] for _ in range(n)]
    visited[0][0] = 0
    arr = [(0, 0, 0)]

    while len(arr) != 0:
        dist, x, y = heappop(arr)

        if x == n - 1 and y == n - 1:
            return dist

        if dist > visited[x][y]:
            continue

        for (dir_x, dir_y) in dirmap:
            new_x, new_y = x + dir_x, y + dir_y

            if 0 <= new_x < n and 0 <= new_y < n and maze[new_x][new_y] != "#":
                new_dist = dist + 1
                if new_dist < visited[new_x][new_y]:
                    visited[new_x][new_y] = new_dist
                    heappush(arr, (new_dist, new_x, new_y))

    return -1


for i in range(fallen_bytes):
    x, y = [int(c) for c in lines[i].split(",")]
    maze[y][x] = "#"

start_time = time.time()
print("Part 1:", walk(n))
print(time.time() - start_time, "seconds")
print()

# part 2
start_time = time.time()
for i in range(fallen_bytes, len(lines)):
    x, y = [int(c) for c in lines[i].split(",")]
    maze[y][x] = "#"

    if walk(n) == -1:
        print(f"Part2: {x},{y}")
        print(time.time() - start_time, "seconds")
        break
