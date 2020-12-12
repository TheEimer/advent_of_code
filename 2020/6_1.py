data = []
with open("/home/eimer/Dokumente/advent_of_code_2020/data_6.txt", "r") as fp:
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
print(count)
