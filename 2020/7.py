def count_insides(bag_name):
    bag = None
    for i in range(len(data)):
        if data[i].strip().startswith(bag_name):
            bag = data[i]
    if "no other" in bag:
        return 1
    else:
        line = bag.split(" ")
        insides = [line[5+i*4] + " " + line[6+i*4] for i in range(len(line[4:])//4)]
        counts = [int(line[4+i*4]) for i in range(len(line[4:])//4)]
        total = sum([counts[i]*count_insides(insides[i]) for i in range(len(insides))])
        return total + 1

with open("data/data_7.txt", "r") as fp:
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
print(f"Part 1: {count}")
print(f"Part 2: {count_insides('shiny gold')-1}")
