import functools
import math
from typing import Dict

with open("test.txt") as f:
    lines = f.read().splitlines()

splitter = lines.index('')
rules = lines[:splitter]
manuals = lines[splitter+1:]

rulemap: Dict[str, list] = {}

for rule in rules:
    first, second = [x for x in rule.split("|")]

    if first not in rulemap:
        rulemap[first] = []

    rulemap[first].append(second)

total = 0
total2 = 0


def sort_fn(a, b):
    if a in rulemap and b in rulemap[a]:
        return -1
    elif b in rulemap and a in rulemap[b]:
        return 1
    else:
        return 0


for m in manuals:
    pages = m.split(",")
    size = len(pages)
    is_ok = True

    for i in range(size):
        page = pages[i]

        if page in rulemap:
            for r in rulemap[page]:
                try:
                    search = pages.index(r)

                    if search < i:
                        is_ok = False
                        break
                except:
                    # rule not present in this manual
                    continue

        if not is_ok:
            break

    if is_ok:
        total += int(pages[math.ceil((size-1) / 2)])
    else:  # part 2
        fixed = sorted(pages, key=functools.cmp_to_key(sort_fn))
        total2 += int(fixed[math.ceil((size-1) / 2)])

print("part 1", total)
print("part 2", total2)
