import time

with open("test.txt") as f:
    lines = f.read().splitlines()

sep = lines.index("")
gates: dict[str, int] = {}
ops = []
z_gates = []


def get_value(g1: str, g2: str, op: str) -> int:
    if op == "XOR":
        return gates[g1] ^ gates[g2]
    elif op == "AND":
        return gates[g1] & gates[g2]
    else:
        return gates[g1] | gates[g2]


start_time = time.time()
# get the x and y gates values
for i in range(sep):
    gate, value = lines[i].split(": ")
    gates[gate] = int(value)

# while parsing the operations, calculate those we already can
for i in range(sep+1, len(lines)):
    g1, op, g2, arrow, out = lines[i].split(" ")
    if out.startswith("z"):
        z_gates.append(out)

    if g1 in gates and g2 in gates:
        gates[out] = get_value(g1, g2, op)
    else:
        ops.append((g1, g2, op, out))

# loop over the gates operations until all of them are evaluated
idx = 0
while len(ops) != 0:
    if idx >= len(ops):
        idx = 0

    if ops[idx][0] in gates and ops[idx][1] in gates:
        g1, g2, op, out = ops.pop(idx)
        gates[out] = get_value(g1, g2, op)
    else:
        idx += 1

# set the bits of the final answer
number = 0
for z in z_gates:
    if gates[z] == 1:
        bit = int(z[1:])
        number = number | (1 << bit)

print(number)
print(time.time() - start_time, "seconds")
