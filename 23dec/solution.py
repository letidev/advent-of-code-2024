import time

with open("test.txt") as f:
    lines = f.read().splitlines()

nodes: dict[str, list[str]] = {}

for line in lines:
    n1, n2 = line.split("-")

    if n1 not in nodes:
        nodes[n1] = []
    if n2 not in nodes:
        nodes[n2] = []

    nodes[n1].append(n2)
    nodes[n2].append(n1)

# part 1
start_time = time.time()
threes = 0
for node in nodes:
    for i in range(len(nodes[node]) - 1):
        for j in range(i+1, len(nodes[node])):
            adj1 = nodes[node][i]
            adj2 = nodes[node][j]

            if adj2 in nodes[adj1] and (node.startswith("t") or adj1.startswith("t") or adj2.startswith("t")):
                threes += 1

threes = int(threes / 3)
print(threes)
print(time.time() - start_time, "seconds")
print()

# part 2
start_time = time.time()
C = []


def walk(R:  set[str], X:  set[str], P: set[str]):
    if len(P) == 0 and len(X) == 0 and len(R) > 2:
        C.append(sorted(R))
        return

    for v in P.union(set()):
        walk(R.union([v]), X.intersection(
            set(nodes[v])), P.intersection(nodes[v]))
        P.remove(v)
        X.add(v)


walk(set(), set(), set(nodes.keys()))

party = []

for c in C:
    if len(c) > len(party):
        party = c

print(",".join(party))
print(time.time() - start_time, "seconds")
