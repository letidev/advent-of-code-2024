import time

with open("example.txt") as f:
    maze = f.read().splitlines()

inf = float('inf')
n = len(maze)
m = len(maze[0])
dirmap = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # up, left, down, right
scores = [[[inf] * 4 for _ in range(m)] for _ in range(n)]


def walk(arr, scores):
    while len(arr) != 0:
        cell, dir = arr.pop()

        if maze[cell[0]][cell[1]] == 'E':
            continue

        for new_dir, (dir_x, dir_y) in enumerate(dirmap):
            if (new_dir + 2) % 4 == dir:
                # 180 deg turn
                continue

            new_x, new_y = cell[0] + dir_x, cell[1] + dir_y

            if maze[new_x][new_y] == "#":
                continue

            turn_cost = 0 if dir == new_dir else 1000
            score = scores[cell[0]][cell[1]][dir] + 1 + turn_cost

            if score < scores[new_x][new_y][new_dir]:
                scores[new_x][new_y][new_dir] = score
                arr.append(((new_x, new_y), new_dir))

    return min(scores[1][m-2])


start_time = time.time()

scores[n-2][1][3] = 0
arr = [((n-2, 1), 3)]

minscore = walk(arr, scores)

print(time.time() - start_time, "seconds")
print(minscore)
