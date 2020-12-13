import itertools

def is_sum(number, batch):
    for j in itertools.combinations(batch, 2):
        if j[0] + j[1] == number:
            return True
    return False


with open("data/data_9.txt", "r") as fp:
    data = fp.readlines()

batch = []
for i in range(len(data)):
    line = data[i].strip()
    if len(batch) < 25:
        batch.append(int(line))
        continue
    number = int(line)
    if not is_sum(number, batch):
        print(f"Part 1: {number}")
        break
    else:
        batch.append(number)
        batch = batch[1:]

data = [int(d.strip()) for d in data]
i = 0
j = 2
solved = False
while not solved:
    if sum(data[i:j]) == 22477624 and i+1 < j:
        solution = data[i:j]
        print(f"Part 2: {max(solution) + min(solution)}")
        solved = True
    elif sum(data[i:j]) > 22477624:
        i += 1
    elif j < len(data):
        j += 1
    else:
        solved = True
        print("error")

