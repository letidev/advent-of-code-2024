import time

with open("test.txt") as f:
    lines = f.read().splitlines()

towels = lines[0].split(", ")

desired = lines[2:]
possible = 0

start = time.time()
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

    arr: list[tuple[int, list]] = []
    visited = [0 for _ in range(len(d)+1)]

    for n in nodes[0]:
        arr.append((n, [0]))

    while len(arr) != 0:
        n, path = arr.pop()

        if n == len(d):
            for node in path:
                visited[node] += 1
            continue

        elif visited[n] != 0:
            for node in path:
                visited[node] += visited[n]

            continue

        path.append(n)

        for next in nodes[n]:
            arr.append((next, path.copy()))

    possible += visited[0]

print(time.time() - start, "seconds")
print(possible)
