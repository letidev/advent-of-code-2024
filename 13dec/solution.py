with open("test.txt") as f:
    lines = f.read().splitlines()

games: list[list[tuple[int, int]]] = []
gameId = 0
c = 0

for line in lines:
    xy = ""
    if c < 3:
        if c == 0:
            games.append([])
            xy = line[10:]
        elif c == 1:
            xy = line[10:]
        elif c == 2:
            xy = line[7:]

        x, y = [x[2:] for x in xy.split(", ")]
        if c != 2:
            games[gameId].append((int(x), int(y)))
        else:
            games[gameId].append(
                (int(x) + 10000000000000, int(y) + 10000000000000))
    else:
        gameId += 1
        c = -1

    c += 1

gameId += 1
total = 0
for g in range(gameId):
    a = games[g][0]
    b = games[g][1]
    p = games[g][2]

    p1 = a[1] * p[0]
    m1 = a[1] * b[0]

    p2 = a[0] * p[1]
    m2 = a[0] * b[1]

    pt = abs(p1-p2)
    mt = abs(m1-m2)

    if pt % mt == 0:
        m = int(pt/mt)
        diff = p[0] - m*b[0]
        if diff % a[0] == 0:
            n = int(diff / a[0])
            total += (3*n + m)

print(total)
