data = []
with open("/home/eimer/Dokumente/advent_of_code_2020/data_7.txt", "r") as fp:
    data = fp.readlines()

containers = ["shiny gold"]
count = 0
start_count = 100
while start_count != count:
    start_count = count
    for i in range(len(data)):
        line = data[i].strip()
        line = line.split(" ")
        color = line[0] + " " + line[1]
        if color in containers:
            continue
        inside = [line[5+i*4] +" " + line[6+i*4] for i in range(len(line[4:])//4)] 
        is_inside = [c in inside for c in containers]
        if any(is_inside):
            count += 1
            containers.append(color)
print(count)
