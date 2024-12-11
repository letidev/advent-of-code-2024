import time

with open("test.txt") as f:
    stones = f.read().split()

start_time = time.time()
for _ in range(25):
    i = 0
    while i < len(stones):
        if stones[i] == '0':
            stones[i] = '1'
            i += 1
        elif len(stones[i]) % 2 == 0:
            size = len(stones[i])
            left = stones[i][0:int(size/2)]
            right = stones[i][int(size/2):]
            right = str(int(right))  # to trim leading zeroes
            stones[i] = left
            stones.insert(i+1, right)
            i += 2
        else:
            stones[i] = str(int(stones[i]) * 2024)
            i += 1

print(time.time() - start_time, "seconds")
print(len(stones))
