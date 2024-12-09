import time

with open("test.txt") as f:
    diskmap = f.read()

fs = []
fid = 0

start_time = time.time()
for i in range(len(diskmap)):
    size = int(diskmap[i])
    if i % 2 == 0:
        fs.extend([fid for _ in range(size)])
        fid += 1
    else:
        fs.extend(["." for _ in range(size)])

n = len(fs)
left = 0
right = n-1

while left < right:
    if fs[left] == "." and fs[right] != ".":
        fs[left] = fs[right]
        fs[right] = "."
        left += 1
        right -= 1
    else:
        if fs[left] != ".":
            left += 1
        if fs[right] == ".":
            right -= 1

checksum = 0
for i in range(n):
    if fs[i] != ".":
        checksum += i * fs[i]
    else:
        break

print(time.time() - start_time, "seconds")
print(checksum)
