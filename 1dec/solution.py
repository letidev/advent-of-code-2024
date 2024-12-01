lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()


arr1 = []
arr2 = []
for i in range(len(lines)):
    line = lines[i].split()

    arr1.append(int(line[0]))
    arr2.append(int(line[1]))


arr1.sort()
arr2.sort()

dist = 0

for i in range(len(arr1)):
    dist += abs(arr1[i] - arr2[i])

print("part 1:", dist)

# ==========

map = {}

dist2 = 0
for i in range(len(arr1)):
    if arr1[i] in map:
        dist2 += arr1[i] * map[arr1[i]]
    else:
        map[arr1[i]] = arr2.count(arr1[i])
        dist2 += arr1[i] * map[arr1[i]]

print("part 2:", dist2)
