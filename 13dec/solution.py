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
        games[gameId].append((int(x), int(y)))
    else:
        gameId += 1
        c = -1

    c += 1

gameId += 1
mins = [None for _ in range(gameId)]
for g in range(gameId):
    a = games[g][0]
    b = games[g][1]
    p = games[g][2]
    for i in range(101):
        for j in range(101):
            if a[0]*i + b[0]*j == p[0] and a[1]*i + b[1]*j == p[1]:
                cost = i*3 + j
                if mins[g] == None:
                    mins[g] = cost
                else:
                    mins[g] = min(mins[g], cost)

total = sum([m if m != None else 0 for m in mins])
print(total)
