import time

with open("test.txt") as f:
    stones = f.read().split()

dp: list[dict[str, int]] = [{} for _ in range(100)]


def count(stone: str, blink: int) -> int:
    if blink == 0:
        return 1

    memo = dp[blink]

    if stone in memo:
        return memo[stone]

    if stone == '0':
        memo[stone] = count('1', blink-1)
    elif len(stone) % 2 == 0:
        size = len(stone)
        left = stone[0:int(size/2)]
        right = stone[int(size/2):]
        right = str(int(right))  # to trim leading zeroes
        memo[stone] = count(left, blink-1) + count(right, blink-1)
    else:
        new = str(int(stone) * 2024)
        memo[stone] = count(new, blink-1)

    return memo[stone]


start_time = time.time()
total25 = 0
total75 = 0
for stone in stones:
    total25 += count(stone, 25)
    total75 += count(stone, 75)


print(time.time() - start_time, "seconds")
print("part 1", total25)
print("part 2", total75)
