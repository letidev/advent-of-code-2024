with open("test.txt") as f:
    lines = f.read().splitlines()


def eq(n, pos, nums, tv, sum, calcs) -> bool:
    if pos == n:
        calcs.append(sum)
        return

    eq(n, pos+1, nums, tv, sum + nums[pos], calcs)
    eq(n, pos+1, nums, tv, sum * nums[pos], calcs)
    eq(n, pos+1, nums, tv, int(f"{sum}{nums[pos]}"), calcs)


total = 0
for line in lines:
    tv, operation = line.split(": ")
    tv = int(tv)
    nums = [int(x) for x in operation.split(" ")]

    calcs = []
    eq(len(nums), 1, nums, tv, nums[0], calcs)

    if tv in calcs:
        total += tv

print(total)
