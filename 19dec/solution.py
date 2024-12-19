with open("test.txt") as f:
    lines = f.read().splitlines()

towels = lines[0].split(", ")

desired = lines[2:]
possible = 0

for d in desired:
    nodes = [[] for _ in range(len(d)+1)]

    for t in towels:
        i = 0
        while i != -1:
            i = d.find(t, i)
            if i != -1:
                nodes[i].append(i + len(t))
                i += 1

    if len(nodes[0]) == 0:
        continue

    arr = []
    for n in nodes[0]:
        arr.append(n)

    while len(arr) != 0:
        n = arr.pop()

        if n == len(d):
            possible += 1
            break

        for next in nodes[n]:
            arr.append(next)

print(possible)
