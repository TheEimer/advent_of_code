from toolz import memoize

@memoize
def count_combos(rest):
    if len(rest) <= 2:
        return 1
    start, rest = rest[0], rest[1:]
    return sum(count_combos(r) for r in map(lambda n: rest[n:], range(len(rest))) if r[0] - 3 <= start)

data = []
with open("/home/eimer/Dokumente/advent_of_code_2020/data_10.txt", "r") as fp:
    data = fp.readlines()

data = sorted([int(d.strip()) for d in data])
data.insert(0, 0)
data.append(data[-1]+3)
print(count_combos(tuple(data)))
