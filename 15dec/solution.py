with open("test.txt") as f:
    lines = f.read().splitlines()

grid = []
inst = ""
boxes = []

dirmap = {
    "^": (-1, 0),
    "v": (1, 0),
    ">": (0, 1),
    "<": (0, -1),
}

robot = (-1, -1)


def move_horizontal(robot: tuple[int, int], direction: tuple[int, int]) -> tuple[int, int]:
    can_move = False
    pos = robot

    while grid[pos[0]][pos[1]] != "#":
        char = grid[pos[0]][pos[1]]

        if char == ".":
            can_move = True
            break

        pos = (pos[0] + direction[0], pos[1] + direction[1])

    if can_move:
        line = ''.join(grid[pos[0]])
        if pos < robot:
            cut = line[pos[1]: robot[1] + 1]
            line = line.replace(cut, f"{cut[1:]}.", 1)
        else:
            cut = line[robot[1]: pos[1] + 1]
            line = line.replace(cut, f".{cut[0:-1]}", 1)

        grid[pos[0]] = list(line)
        robot = (robot[0] + direction[0], robot[1] + direction[1])

    return robot


def move_vertical(robot: tuple[int, int], direction: tuple[int, int]) -> tuple[int, int]:

    # easy case - move to empty space
    if grid[robot[0] + direction[0]][robot[1]+direction[1]] == ".":
        grid[robot[0]][robot[1]] = "."
        robot = (robot[0] + direction[0], robot[1]+direction[1])
        grid[robot[0]][robot[1]] = "@"
        return robot
    # easy case - do nothing
    elif grid[robot[0] + direction[0]][robot[1]+direction[1]] == "#":
        return robot
    else:
        stack = []
        adj = (robot[0] + direction[0], robot[1]+direction[1])
        layer_size = 1

        if grid[adj[0]][adj[1]] == "[":
            stack.append((adj[0], adj[1]))
        else:
            stack.append((adj[0], adj[1]-1))

        hit_wall = False
        while layer_size != 0:
            hit_wall = False
            to_add = []
            for i in range(len(stack) - layer_size, len(stack)):
                box = stack[i]
                adj = (box[0] + direction[0], box[1] + direction[1])

                if grid[adj[0]][adj[1]] == "#" or grid[adj[0]][adj[1] + 1] == "#":
                    hit_wall = True
                    break

                if grid[adj[0]][adj[1]] == "[":
                    to_add.append((adj[0], adj[1]))

                if grid[adj[0]][adj[1]] == "]":
                    to_add.append((adj[0], adj[1]-1))

                if grid[adj[0]][adj[1]+1] == "[":
                    to_add.append((adj[0], adj[1]+1))

            if hit_wall:
                break

            stack.extend(to_add)
            layer_size = len(to_add)

        if not hit_wall:
            size = len(stack)
            for _ in range(size):
                box = stack.pop()
                grid[box[0]][box[1]] = "."
                grid[box[0]][box[1]+1] = "."
                grid[box[0] + direction[0]][box[1]+direction[1]] = "["
                grid[box[0] + direction[0]][box[1]+direction[1]+1] = "]"
            grid[robot[0]][robot[1]] = "."
            robot = (robot[0]+direction[0], robot[1]+direction[1])
            grid[robot[0]][robot[1]] = "@"

    return robot


flag = False
for i in range(len(lines)):
    line = lines[i]
    if line == "":
        flag = True

    if not flag:
        new_line = ""
        j = 0
        for c in line:
            if c == "#":
                new_line = f"{new_line}##"
            elif c == "O":
                boxes.append((i, j))
                new_line = f"{new_line}[]"
            elif c == ".":
                new_line = f"{new_line}.."
            else:
                robot = (i, j)
                new_line = f"{new_line}@."

            j += 2

        grid.append(list(new_line))
    else:
        inst = f"{inst}{line}"

for instruction in inst:
    direction = dirmap[instruction]
    if direction[0] == 0:
        robot = move_horizontal(robot, direction)
    else:
        robot = move_vertical(robot, direction)

gps = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "[":
            gps += 100*i + j

print(gps)
