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
        
data = []
with open("/home/eimer/Dokumente/advent_of_code_2020/data_7.txt", "r") as fp:
    data = fp.readlines()

print(count_insides("shiny gold")-1)
