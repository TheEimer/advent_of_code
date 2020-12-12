def is_loop():
    visited_steps = []
    cur = 0
    while not cur in visited_steps:
        visited_steps.append(cur)
        if cur >= len(data):
            return False
        line = data[cur].strip()
        if "jmp" in line:
            cur += int(line.split(" ")[1]) 
        else:
            cur += 1
    return True

data = []
with open("/home/eimer/Dokumente/advent_of_code_2020/data_8.txt", "r") as fp:
    data = fp.readlines()

for i in range(len(data)):
    line = data[i].strip()
    if "nop" in line:
        data[i] = "jmp " + line.split(" ")[1]
        if is_loop():
            data[i] = line
        else:
            break
    elif "jmp" in line:
        data[i] = "nop " + line.split(" ")[1]
        if is_loop():
            data[i] = line
        else:
            break
        
accumulator = 0
done = False
step = 0
while not done:
    line = data[step].strip()
    if "jmp" in line:
        step += int(line.split(" ")[1])
    elif "acc" in line:
        accumulator += int(line.split(" ")[1])
        step += 1
    else:
        step += 1
    if step >= len(data):
        done = True
print(accumulator)
