data = []
with open("/home/eimer/Dokumente/advent_of_code_2020/data_10.txt", "r") as fp:
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
print(ones*threes)

