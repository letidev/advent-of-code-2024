lines = []
with open("test.txt") as f:
    lines = f.read().splitlines()


def is_safe(line: list[int]):
    dist = [line[i] - line[i+1] for i in range(len(line) - 1)]

    pos = sum([1 for x in dist if x > 0])
    neg = sum([1 for x in dist if x < 0])
    wrong = sum([1 for x in dist if x == 0 or abs(x) > 3])

    if wrong == 0 and ((pos == 0 and neg != 0) or (pos != 0 and neg == 0)):
        return True
    return False


safe_reports = 0
for i in range(len(lines)):
    line = [int(x) for x in lines[i].split()]

    if (is_safe(line)):  # part 1
        safe_reports += 1
    else:  # part 2
        for j in range(len(line)):
            trunc = [line[x] for x in range(len(line)) if x != j]

            if is_safe(trunc):
                safe_reports += 1
                break

print(safe_reports)
