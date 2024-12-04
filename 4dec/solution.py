lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()

n = len(lines)
m = len(lines[0])

# part 1
total = 0
for i in range(n):
    for j in range(m):
        # horizontal
        if j + 3 < m:
            # normal
            if lines[i][j] == "X" and lines[i][j+1] == "M" and lines[i][j+2] == "A" and lines[i][j+3] == "S":
                total += 1

            # flipped
            if lines[i][j] == "S" and lines[i][j+1] == "A" and lines[i][j+2] == "M" and lines[i][j+3] == "X":
                total += 1

        # vertical
        if i + 3 < n:
            # normal
            if lines[i][j] == "X" and lines[i+1][j] == "M" and lines[i+2][j] == "A" and lines[i+3][j] == "S":
                total += 1

            # flipped
            if lines[i][j] == "S" and lines[i+1][j] == "A" and lines[i+2][j] == "M" and lines[i+3][j] == "X":
                total += 1

        # left diagonal
        if i + 3 < n and j + 3 < m:
            # normal
            if lines[i][j] == "X" and lines[i+1][j+1] == "M" and lines[i+2][j+2] == "A" and lines[i+3][j+3] == "S":
                total += 1

            # flipped
            if lines[i][j] == "S" and lines[i+1][j+1] == "A" and lines[i+2][j+2] == "M" and lines[i+3][j+3] == "X":
                total += 1

        # right diagonal
        if i + 3 < n and j - 3 >= 0:
            # normal
            if lines[i][j] == "X" and lines[i+1][j-1] == "M" and lines[i+2][j-2] == "A" and lines[i+3][j-3] == "S":
                total += 1

            # flipped
            if lines[i][j] == "S" and lines[i+1][j-1] == "A" and lines[i+2][j-2] == "M" and lines[i+3][j-3] == "X":
                total += 1

print("part 1", total)

# part 2

# M . S
# . A .
# M . S

total = 0
for i in range(n):
    for j in range(m):
        if i + 2 < n and j + 2 < m:
            if lines[i+1][j+1] == "A" and ((lines[i][j] == "M" and lines[i+2][j+2] == "S") or (lines[i][j] == "S" and lines[i+2][j+2] == "M")) and ((lines[i][j+2] == "M" and lines[i+2][j] == "S") or (lines[i][j+2] == "S" and lines[i+2][j] == "M")):
                total += 1

print("part 2", total)
