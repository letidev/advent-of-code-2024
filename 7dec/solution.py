import time

with open("test.txt") as f:
    lines = f.read().splitlines()


def eq(n, pos, nums, sum, tv) -> bool:
    if sum > tv:
        return False
    if pos == n:
        return sum == tv

    return eq(n, pos+1, nums, sum + nums[pos], tv) or \
        eq(n, pos+1, nums, sum * nums[pos], tv) or \
        eq(n, pos+1, nums, int(f"{sum}{nums[pos]}"), tv)


start_time = time.time()
total = 0
for line in lines:
    tv, operation = line.split(": ")
    tv = int(tv)
    nums = [int(x) for x in operation.split(" ")]
    n = len(nums)

    if eq(n, 1, nums, nums[0], tv):
        total += tv

print(time.time() - start_time, "seconds")
print(total)
