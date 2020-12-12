data = []
with open("/home/eimer/Dokumente/advent_of_code_2020/data_3.txt", "r") as fp:
    data = fp.readlines()

trees_11 = 0
width = len(data[0])-1

for i in range(len(data)):
    line = [c for c in data[i]][:-1]
    if line[i%width] == "#":
        trees_11 += 1
print(f"1, 1: {trees_11}")

trees_31 = 0
for i in range(0, len(data)):
    line = [c for c in data[i]][:-1]
    if line[(i*3)%width] == "#":
        trees_31 += 1
print(f"3, 1: {trees_31}")

trees_51 = 0
for i in range(0, len(data)):
    line = [c for c in data[i]][:-1]
    if line[(i*5)%width] == "#":
        trees_51 += 1
print(f"5, 1: {trees_51}") 


trees_71 = 0
for i in range(0, len(data)):
    line = [c for c in data[i]][:-1]
    if line[(i*7)%width] == "#":
        trees_71 += 1
print(f"7, 1: {trees_71}")


trees_12 = 0
for i in range(0, len(data)//2):
    line = [c for c in data[i*2]][:-1]
    if line[i%width] == "#":
        trees_12 += 1
print(f"1, 2: {trees_12}")

print(f"Result: {trees_11*trees_31*trees_51*trees_71*trees_12}")
