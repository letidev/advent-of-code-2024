with open("test.txt") as f:
    lines = f.read().splitlines()

heads = []
n, m = len(lines), len(lines[0])
dp_score = [[0 for _ in range(m)] for _ in range(n)]
scores = 0


def get_score(n, m, i, j):
    if (lines[i][j] == 9):
        dp_score[i][j] = 1
        return

    if i > 0 and lines[i][j] + 1 == lines[i-1][j]:
        if dp_score[i-1][j] != 0:
            dp_score[i][j] += dp_score[i-1][j]

        else:
            get_score(n, m, i-1, j)
            dp_score[i][j] += dp_score[i-1][j]

    if i < n - 1 and lines[i][j] + 1 == lines[i+1][j]:
        if dp_score[i+1][j] != 0:
            dp_score[i][j] += dp_score[i+1][j]
        else:
            get_score(n, m, i+1, j)
            dp_score[i][j] += dp_score[i+1][j]

    if j > 0 and lines[i][j] + 1 == lines[i][j-1]:
        if dp_score[i][j-1] != 0:
            dp_score[i][j] += dp_score[i][j-1]
        else:
            get_score(n, m, i, j-1)
            dp_score[i][j] += dp_score[i][j-1]

    if j < m - 1 and lines[i][j] + 1 == lines[i][j+1]:
        if dp_score[i][j+1] != 0:
            dp_score[i][j] += dp_score[i][j+1]
        else:
            get_score(n, m, i, j+1)
            dp_score[i][j] += dp_score[i][j+1]


lines = [[int(line[i]) for i in range(m)] for line in lines]

for i in range(n):
    for j in range(m):
        if lines[i][j] == 0:
            heads.append((i, j))

for head in heads:
    get_score(n, m, head[0], head[1])
    scores += dp_score[head[0]][head[1]]

# for i in range(n):
#     for j in range(m):
#         print(dp_score[i][j], end='  ')
#     print()

print(scores)
