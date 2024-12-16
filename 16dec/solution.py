import time

from colorama import Fore, Style
from colorama import init as colorama_init

colorama_init()

with open("example.txt") as f:
    maze = f.read().splitlines()

inf = float('inf')
n = len(maze)
m = len(maze[0])
dirmap = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # up, left, down, right
scores = [[[inf] * 4 for _ in range(m)] for _ in range(n)]


def walk(arr, scores):
    while len(arr) != 0:
        x, y, dir = arr.pop()

        if maze[x][y] == 'E':
            continue

        for new_dir, (dir_x, dir_y) in enumerate(dirmap):
            if (new_dir + 2) % 4 == dir:
                # 180 deg turn
                continue

            new_x, new_y = x + dir_x, y + dir_y

            if maze[new_x][new_y] == "#":
                continue

            turn_cost = 0 if dir == new_dir else 1000
            score = scores[x][y][dir] + 1 + turn_cost

            if score < scores[new_x][new_y][new_dir]:
                scores[new_x][new_y][new_dir] = score
                arr.append((new_x, new_y, new_dir))

    return min(scores[1][m-2])


def find_best(arr, scores):
    best = set()

    while len(arr) != 0:
        x, y, dir = arr.pop()
        best.add((x, y))

        # move backwards
        adj_x, adj_y = x - dirmap[dir][0], y - dirmap[dir][1]

        if maze[adj_x][adj_y] == "#":
            continue

        for adj_dir in range(4):

            turn_cost = 0 if dir == adj_dir else 1000
            expected = scores[adj_x][adj_y][adj_dir] + 1 + turn_cost

            if expected == scores[x][y][dir]:
                arr.append((adj_x, adj_y, adj_dir))

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if ((i, j) in best):
                print(f"{Fore.GREEN}O{Style.RESET_ALL}", end=" ")
            else:
                print(maze[i][j], end=" ")
        print()

    return len(best)


start_time = time.time()

scores[n-2][1][3] = 0
arr = [(n-2, 1, 3)]

minscore = walk(arr, scores)

print(time.time() - start_time, "seconds")
print(minscore)

start_time = time.time()

arr = [(1, m-2, d)
       for d in range(4) if scores[1][m-2][d] == min(scores[1][m-2])]
best_tiles = find_best(arr, scores)

print(time.time() - start_time, "seconds")
print(best_tiles)
