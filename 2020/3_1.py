data = []
with open("/home/eimer/Dokumente/advent_of_code_2020/data_3.txt", "r") as fp:
    data = fp.readlines()

trees = 0
width = len(data[0])-1
for i in range(len(data)):
    line = [c for c in data[i]][:-1]
    if line[(i*3)%width] == "#":
        trees += 1
print(trees)
