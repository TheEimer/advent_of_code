data = []
with open("/home/eimer/Dokumente/advent_of_code_2020/data_8.txt", "r") as fp:
    data = fp.readlines()

step = 0
accumulator = 0
visited_steps = []
while not step in visited_steps:
    line = data[step].strip()
    visited_steps.append(step)
    if "acc" in line:
        accumulator += int(line.split(" ")[1])
        step += 1
    elif "jmp" in line:
        step += int(line.split(" ")[1])
    else:
        step += 1
print(accumulator)
