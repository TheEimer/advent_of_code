data = []
with open("/home/eimer/Dokumente/advent_of_code_2020/data_6.txt", "r") as fp:
    data = fp.readlines()

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
print(count)
