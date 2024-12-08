import time

with open("test.txt") as f:
    lines = f.read().splitlines()

# forward approach - 1.4s


def eq(n, pos, nums, sum, tv) -> bool:
    if sum > tv:
        return False
    if pos == n:
        return sum == tv

    return eq(n, pos+1, nums, sum + nums[pos], tv) or \
        eq(n, pos+1, nums, sum * nums[pos], tv) or \
        eq(n, pos+1, nums, int(f"{sum}{nums[pos]}"), tv)


def num_dig(n: int):
    return len(str(n))


# backward approach - 0.02s
def eq2(pos, nums, sum) -> bool:
    if pos == 0:
        return sum == nums[0]

    sub = False
    if nums[pos] < sum:
        sub = eq2(pos-1, nums, sum - nums[pos])

    div = False
    if sum % nums[pos] == 0:
        div = eq2(pos-1, nums, int(sum / nums[pos]))

    glue = False
    digits = num_dig(nums[pos])
    if sum % 10**digits == nums[pos]:
        unglued = str(sum)[:-digits]
        if unglued != '':
            glue = eq2(pos-1, nums, int(unglued))

    return sub or div or glue


start_time = time.time()
total = 0
for line in lines:
    tv, operation = line.split(": ")
    tv = int(tv)
    nums = [int(x) for x in operation.split(" ")]
    n = len(nums)

    # if eq(n, 1, nums, nums[0], tv):
    if eq2(n-1, nums, tv):
        total += tv

print(time.time() - start_time, "seconds")
print(total)
