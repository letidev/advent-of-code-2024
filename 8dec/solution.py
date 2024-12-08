with open("test.txt") as f:
    lines = f.read().splitlines()

antennas: list[tuple] = []
n = len(lines)
m = len(lines[0])
unique = [[False for _ in range(m)] for _ in range(n)]


def in_bounds(i, j, n, m) -> bool:
    return 0 <= i and i < n and 0 <= j and j < m


for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] != ".":
            antennas.append((lines[i][j], i, j))

anti = 0
for i in range(len(antennas) - 1):
    for j in range(i+1, len(antennas)):
        a1 = antennas[i]
        a2 = antennas[j]

        if a1[0] == a2[0]:  # same freq
            di, dj = a2[1] - a1[1], a2[2] - a1[2]
            anti1i, anti1j = a1[1]-di, a1[2]-dj
            anti2i, anti2j = a2[1]+di, a2[2]+dj

            if in_bounds(anti1i, anti1j, n, m) and not unique[anti1i][anti1j]:
                unique[anti1i][anti1j] = True
                anti += 1

            if in_bounds(anti2i, anti2j, n, m) and not unique[anti2i][anti2j]:
                unique[anti2i][anti2j] = True
                anti += 1

print(anti)
