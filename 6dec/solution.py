with open("test.txt") as f:
    lines = f.read().splitlines()

n = len(lines)
m = len(lines[0])

start = (0, 0)
for i in range(n):
    j = lines[i].find("^")
    if j != -1:
        start = (i, j)
        break

total = 0
outside = False
direction = 0
dirmap = [(-1, 0), (0, 1), (1, 0), (0, -1)]


visited_part1 = [[False] * m for _ in range(n)]
guard = start

while not outside:
    cell = lines[guard[0]][guard[1]]
    if cell != "#":
        if not visited_part1[guard[0]][guard[1]]:
            total += 1
            visited_part1[guard[0]][guard[1]] = True
    else:
        guard = (guard[0] - dirmap[direction][0],
                 guard[1] - dirmap[direction][1])
        direction = (direction + 1) % 4

    guard = (guard[0] + dirmap[direction][0], guard[1] + dirmap[direction][1])

    if guard[0] == -1 or guard[0] == n or guard[1] == -1 or guard[1] == m:
        outside = True

print("part 1", total)

# part 2
loops = 0

for r in range(n):
    for c in range(m):
        if lines[r][c] == "." and visited_part1[r][c]:
            obstacle = (r, c)
            visited = [[[False for _ in range(4)]
                        for _ in range(m)] for _ in range(n)]
            direction = 0
            outside = False
            guard = start

            while not outside:
                if lines[guard[0]][guard[1]] == "#" or guard == obstacle:
                    guard = (guard[0] - dirmap[direction][0],
                             guard[1] - dirmap[direction][1])

                    direction = (direction + 1) % 4
                else:
                    if visited[guard[0]][guard[1]][direction]:
                        loops += 1
                        break
                    else:
                        visited[guard[0]][guard[1]][direction] = True

                guard = (guard[0] + dirmap[direction][0],
                         guard[1] + dirmap[direction][1])

                if guard[0] == -1 or guard[0] == n or guard[1] == -1 or guard[1] == m:
                    outside = True

print("part 2", loops)
