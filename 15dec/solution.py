with open("test.txt") as f:
    lines = f.read().splitlines()

grid = []
inst = ""
flag = False

dirmap = {
    "^": (-1, 0),
    "v": (1, 0),
    ">": (0, 1),
    "<": (0, -1),
}

robot = (-1, -1)


def move(robot: tuple[int, int], direction: tuple[int, int]) -> tuple[int, int]:
    can_move = False
    pos = robot

    while grid[pos[0]][pos[1]] != "#":
        char = grid[pos[0]][pos[1]]

        if char == ".":
            can_move = True
            break

        pos = (pos[0] + direction[0], pos[1] + direction[1])

    if can_move:
        # old position of robot always becomes empty space
        grid[robot[0]][robot[1]] = "."

        # calc new robot pos
        robot = (robot[0] + direction[0], robot[1] + direction[1])

        # new robot pos is a box - shift all boxes after robot
        if grid[robot[0]][robot[1]] == "O":
            grid[pos[0]][pos[1]] = "O"

        grid[robot[0]][robot[1]] = "@"

    return robot


for i in range(len(lines)):
    line = lines[i]
    if line == "":
        flag = True

    if not flag:
        j = line.find("@")
        if j != -1:
            robot = (i, j)

        grid.append(list(line))
    else:
        inst = f"{inst}{line}"

for instruction in inst:
    direction = dirmap[instruction]
    robot = move(robot, direction)

gps = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "O":
            gps += 100*i + j

print(gps)
