with open("data/data_3.txt", "r") as fp:
    data = fp.readlines()

trees = 0
width = len(data[0])-1
for i in range(len(data)):
    line = [c for c in data[i]][:-1]
    if line[(i*3)%width] == "#":
        trees += 1
print(f"Part 1: {trees}")

def trees_x1(x):
    trees = 0
    for i in range(0, len(data)):
        line = [c for c in data[i]][:-1]
        if line[(i * 3) % width] == "#":
            trees += 1
    return trees


width = len(data[0])-1

trees_11 = trees_x1(1)
trees_31 = trees_x1(3)
trees_51 = trees_x1(5)
trees_71 = trees_x1(7)
trees_12 = 0
for i in range(0, len(data)//2):
    line = [c for c in data[i*2]][:-1]
    if line[i%width] == "#":
        trees_12 += 1

print(f"Part 2: {trees_11*trees_31*trees_51*trees_71*trees_12}")
