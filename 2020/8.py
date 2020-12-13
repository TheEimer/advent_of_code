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

def run(program):
    step = 0
    accumulator = 0
    visited_steps = []
    done = False
    while not step in visited_steps and not done:
        line = program[step].strip()
        visited_steps.append(step)
        if "acc" in line:
            accumulator += int(line.split(" ")[1])
            step += 1
        elif "jmp" in line:
            step += int(line.split(" ")[1])
        else:
            step += 1
        if step >= len(program):
            done = True
    return  accumulator

with open("data/data_8.txt", "r") as fp:
    data = fp.readlines()

print(f"Part 1: {run(data)}")

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

print(f"Part 2: {run(data)}")
