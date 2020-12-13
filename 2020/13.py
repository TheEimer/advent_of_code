with open("data/data_13.txt", "r") as fp:
    data = fp.readlines()

timestamp = int(data[0])
raw_ids = data[1].strip().split(",")
ids = list(filter(lambda x: x != "x", raw_ids))
ids = list(map(int, ids))
factors = list(map(lambda x: timestamp//x, ids))
next_departures = [ids[i]*(factors[i]+1) for i in range(len(ids))]
next_time = min(next_departures)
best_bus = ids[next_departures.index(next_time)]
print(f"Part 1: {best_bus * (next_time-timestamp)}")

conditions_at_offset = list(map(lambda x: raw_ids.index(str(x)), ids))
times = [0] * len(ids)
products = [ids[0]]
for i in range(1, len(ids)):
    products.append(ids[i]*products[-1])
inverse_products = [products[i]**(ids[i+1]-2)%ids[i+1] for i in range(len(ids)-1)]
for i in range(len(ids)-1):
    coefficient = ((-times[i] - conditions_at_offset[i+1]) * inverse_products[i]) % ids[i+1]
    times[i+1] = times[i] + coefficient * products[i]
print(f"Part 2: {times[-1]}")