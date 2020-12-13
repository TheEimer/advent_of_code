from toolz import memoize

@memoize
def count_combos(rest):
    if len(rest) <= 2:
        return 1
    start, rest = rest[0], rest[1:]
    return sum(count_combos(r) for r in map(lambda n: rest[n:], range(len(rest))) if r[0] - 3 <= start)


with open("data/data_10.txt", "r") as fp:
    data = fp.readlines()

data = sorted([int(d.strip()) for d in data])
ones = 0
threes = 1
if data[0] == 1:
    ones += 1
elif data[9] == 3:
    threes += 1
for i in range(len(data)-1):
    diff = data[i+1] -data[i]
    if diff == 1:
        ones += 1
    elif diff == 3:
        threes += 1
print(f"Part 1: {ones*threes}")

data.insert(0, 0)
data.append(data[-1]+3)
print(f"Part 2: {count_combos(tuple(data))}")

