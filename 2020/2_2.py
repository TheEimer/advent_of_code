data = []
with open("/home/eimer/Dokumente/advent_of_code_2020/data_2.txt", "r") as fp:
    data = fp.readlines()
data = [d.rstrip().split(":") for d in data]
data = [[int(d[0].split(" ")[0].split("-")[0]), int(d[0].split(" ")[0].split("-")[1]), d[0].split(" ")[1], d[1]] for d in data]

valid = 0
for d in data:
    if (d[3][d[0]]==d[2] and not d[3][d[1]]==d[2]) or (d[3][d[1]]==d[2] and not d[3][d[0]]==d[2]):
        valid += 1
print(valid)
