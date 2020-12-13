with open("data/data_6.txt", "r") as fp:
    data = fp.readlines()

yesses = []
count = 0
for i in range(len(data)):
    if not data[i].strip():
        count += len(yesses)
        yesses = []
        continue
    line = data[i].strip()
    for l in line:
        if l not in yesses:
            yesses.append(l)
count += len(yesses)
print(f"Part 1: {count}")

group = []
count = 0
for i in range(len(data)):
    if not data[i].strip():
        intersection = set.intersection(*group)
        count += len(intersection)
        group = []
        continue
    group.append(set(data[i].strip()))

intersection = set.intersection(*group)
count += len(intersection)
print(f"Part 2: {count}")
