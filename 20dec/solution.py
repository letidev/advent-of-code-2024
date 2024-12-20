import time

with open("test.txt") as f:
    maze = f.read().splitlines()

n = len(maze)
m = len(maze[0])

dist = [[-1 for _ in range(m)] for _ in range(n)]
start = (-1, -1)
dirmap = [(1, 0), (0, -1), (-1, 0), (0, 1)]

for i in range(len(maze)):
    s = maze[i].find("S")

    if s != -1:
        start = (i, s)
        break


def get_normal_path(start):
    arr = [(start[0], start[1], 0)]
    path = []

    while len(arr) != 0:
        x, y, d = arr.pop()

        if dist[x][y] != -1:
            continue

        dist[x][y] = d
        path.append((x, y))

        if maze[x][y] == "E":
            break

        for dir_x, dir_y in dirmap:
            new_x, new_y = x + dir_x, y + dir_y
            if dist[new_x][new_y] == -1 and maze[new_x][new_y] != "#":
                arr.append((new_x, new_y, d+1))

    return path


start_time = time.time()
path = get_normal_path(start)
normal_dist = dist[path[-1][0]][path[-1][1]]

cheats = 0
for node in path:
    x, y = node

    for dir_x, dir_y in dirmap:
        wall_x, wall_y = x + dir_x, y + dir_y
        empty_x, empty_y = wall_x + dir_x, wall_y + dir_y

        if maze[wall_x][wall_y] == "#" and 0 <= empty_x < n and 0 <= empty_y < m and maze[empty_x][empty_y] != "#" and dist[empty_x][empty_y] - (dist[x][y] + 2) >= 100:
            cheats += 1

print("Part 1:", cheats)
print(time.time() - start_time, "seconds")
print()

cheats = 0
start_time = time.time()
for i in range(len(path) - 1):
    for j in range(i+1, len(path)):
        sx, sy, = path[i]
        ex, ey = path[j]

        manh = abs(sx-ex) + abs(sy-ey)

        if manh <= 20 and dist[ex][ey] - (dist[sx][sy] + manh) >= 100:
            cheats += 1

print("Part 2", cheats)
print(time.time() - start_time, "seconds")
