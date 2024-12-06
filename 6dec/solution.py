with open("test.txt") as f:
    lines = f.read().splitlines()

n = len(lines)
m = len(lines[0])

startR = 0
startC = 0
for i in range(n):
    j = lines[i].find("^")
    if j != -1:
        startR, startC = i, j
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


visited_part1 = [[False] * m for _ in range(n)]
guardR = startR
guardC = startC

while not outside:
    cell = lines[guardR][guardC]
    if cell != "#":
        if not visited_part1[guardR][guardC]:
            total += 1
            visited_part1[guardR][guardC] = True
    else:
        guardR -= dirmap[direction][0]
        guardC -= dirmap[direction][1]
        direction = (direction + 1) % 4

    guardR += dirmap[direction][0]
    guardC += dirmap[direction][1]

    if guardR == -1 or guardR == n or guardC == -1 or guardC == m:
        outside = True

print("part 1", total)

# part 2
loops = 0

for r in range(n):
    for c in range(m):
        if lines[r][c] == "." and visited_part1[r][c]:
            oi = r  # obstacle row
            oj = c  # obstacle col
            visited = [[[False for _ in range(4)]
                        for _ in range(m)] for _ in range(n)]
            direction = 0
            outside = False
            guardR = startR
            guardC = startC

            while not outside:
                cell = lines[guardR][guardC]

                # if stepped on an obstacle
                if cell == "#" or (guardR == oi and guardC == oj):
                    # take a step back
                    guardR -= dirmap[direction][0]
                    guardC -= dirmap[direction][1]

                    # change direction
                    direction = (direction + 1) % 4
                else:
                    if visited[guardR][guardC][direction]:
                        loops += 1
                        break
                    else:
                        visited[guardR][guardC][direction] = True

                # move towards new direction
                guardR += dirmap[direction][0]
                guardC += dirmap[direction][1]

                if guardR == -1 or guardR == n or guardC == -1 or guardC == m:
                    outside = True

print("part 2", loops)
