import re

with open("test.txt") as f:
    seq = f.read()

matches = re.findall(
    r'(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\))', seq)

sum = 0
enabled = True
for m in matches:
    if "do()" in m[0]:
        enabled = True
    elif "don't()" in m[0]:
        enabled = False
    elif enabled == True:
        sum += int(m[1]) * int(m[2])

print(sum)
