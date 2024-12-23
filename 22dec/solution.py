with open("test.txt") as f:
    buyers = [int(x) for x in f.read().splitlines()]

MOD = 16777216


def get_next(number: int):
    secret = ((number * 64) ^ number) % MOD
    secret = (int(secret / 32) ^ secret) % MOD
    secret = ((secret * 2048) ^ secret) % MOD
    return secret


sequences = {}
seq = []
for i in range(len(buyers)):

    for j in range(2000):
        old_price = buyers[i] % 10
        buyers[i] = get_next(buyers[i])
        new_price = buyers[i] % 10
        seq.append(new_price - old_price)

        if len(seq) == 4:
            key = ','.join([str(x) for x in seq])

            if key not in sequences:
                sequences[key] = [None for _ in range(len(buyers))]

            if sequences[key][i] == None:
                sequences[key][i] = new_price

            seq.pop(0)


print("Part 1", sum(buyers))

res = 0
for key in sequences:
    bananas = 0
    for b in sequences[key]:
        bananas += b if b != None else 0

    if bananas > res:
        res = bananas

print("Part 2", res)
