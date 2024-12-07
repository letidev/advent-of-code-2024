import time

with open("test.txt") as f:
    lines = f.read().splitlines()


def eq(n, pos, nums, sum, calcs) -> bool:
    if pos == n:
        calcs.append(sum)
        return

    eq(n, pos+1, nums, sum + nums[pos], calcs)
    eq(n, pos+1, nums, sum * nums[pos], calcs)
    eq(n, pos+1, nums, int(f"{sum}{nums[pos]}"), calcs)


start_time = time.time()
total = 0
for line in lines:
    tv, operation = line.split(": ")
    tv = int(tv)
    nums = [int(x) for x in operation.split(" ")]
    n = len(nums)

    calcs = []
    eq(n, 1, nums, nums[0], calcs)

    if tv in calcs:
        total += tv

print(time.time() - start_time, "seconds")
print(total)
