with open("test.txt") as f:
    lines = f.read().splitlines()

n = len(lines)
m = len(lines[0])

guardR = 0
guardC = 0
for i in range(n):
    j = lines[i].find("^")
    if j != -1:
        guardR = i
        guardC = j
        break

total = 0
outside = False
direction = 0
dirmap = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}


visited = [[False] * m for _ in range(n)]

while not outside:
    cell = lines[guardR][guardC]
    if cell != "#":
        if not visited[guardR][guardC]:
            total += 1
            visited[guardR][guardC] = True
    else:
        guardR -= dirmap[direction][0]
        guardC -= dirmap[direction][1]
        direction = (direction + 1) % 4

    guardR += dirmap[direction][0]
    guardC += dirmap[direction][1]

    if guardR == -1 or guardR == len(lines) or guardC == -1 or guardC == len(lines[0]):
        outside = True

print(total)
