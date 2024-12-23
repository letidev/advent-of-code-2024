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
