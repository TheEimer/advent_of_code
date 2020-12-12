data = []
with open("/home/eimer/Dokumente/advent_of_code_2020/data_1_1.txt", "r") as fp:
    data = fp.readlines()
data = [int(d) for d in data]

for i in data:
    for j in data:
        if i!=j and i+j==2020:
            print(i*j)
