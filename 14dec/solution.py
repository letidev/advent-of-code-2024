import math
import time

with open("test.txt") as f:
    lines = f.read().splitlines()

robots = []
# example
# cols = 11
# rows = 7

# test
cols = 101
rows = 103

mid_x = int(math.floor(cols/2))
mid_y = int(math.floor(rows/2))

for line in lines:
    p, v = line.split(" ")
    p, v = p[2:], v[2:]
    p = [int(x) for x in p.split(",")]
    v = [int(x) for x in v.split(",")]

    robots.append({
        "p": p,
        "v": v
    })


def move(robot):
    p = robot["p"]
    v = robot["v"]

    move_x = (p[0] + v[0]) % cols
    move_y = (p[1] + v[1]) % rows

    if move_x < 0:
        move_x = cols + move_x

    if move_y < 0:
        move_y = rows + move_y

    p[0] = move_x
    p[1] = move_y


# part 1
q1, q2, q3, q4 = 0, 0, 0, 0
start_time = time.time()
for robot in robots:
    p = robot["p"]
    v = robot["v"]

    move_x = (p[0] + v[0]*100) % cols
    move_y = (p[1] + v[1]*100) % rows

    if move_x < 0:
        move_x = cols + move_x

    if move_y < 0:
        move_y = rows + move_y

    if move_x > mid_x and move_y < mid_y:  # top right
        q1 += 1

    if move_x < mid_x and move_y < mid_y:  # top left
        q2 += 1

    if move_x < mid_x and move_y > mid_y:  # bottom left
        q3 += 1

    if move_x > mid_x and move_y > mid_y:  # bottom right
        q4 += 1

print(time.time() - start_time, "seconds")
print(q1 * q2 * q3 * q4)

# part 2
start_time = time.time()
all_unique = False
seconds = 0

stars = [[False for _ in range(cols)] for _ in range(rows)]

while not all_unique:
    arr = []
    for robot in robots:
        move(robot)
        arr.append((robot["p"][0], robot["p"][1]))

    seconds += 1
    if len(arr) == len(set(arr)):
        all_unique = True

        for robot in robots:
            stars[robot["p"][1]][robot["p"][0]] = True

print(time.time() - start_time, "seconds")
print(seconds)

# print the christmas tree
for i in range(rows):
    for j in range(cols):
        if stars[i][j]:
            print("*", end="")
        else:
            print(".", end="")
    print()
