import math

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

q1, q2, q3, q4 = 0, 0, 0, 0
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

print(q1 * q2 * q3 * q4)
