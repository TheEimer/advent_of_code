import itertools

def is_sum(number, batch):
    for j in itertools.combinations(batch, 2):
        if j[0] + j[1] == number:
            return True
    return False

data = []
with open("/home/eimer/Dokumente/advent_of_code_2020/data_9.txt", "r") as fp:
    data = fp.readlines()

batch = []
for i in range(len(data)):
    line = data[i].strip()
    if len(batch) < 25:
        batch.append(int(line))
        continue
    number = int(line)
    if not is_sum(number, batch):
        print(number)
        break
    else:
        batch.append(number)
        batch = batch[1:]

