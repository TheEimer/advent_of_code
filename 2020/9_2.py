data = []
with open("/home/eimer/Dokumente/advent_of_code_2020/data_9.txt", "r") as fp:
    data = fp.readlines()

data = [int(d.strip()) for d in data]
i = 0
j = 2
solved = False
while not solved:
    if sum(data[i:j]) == 22477624 and i+1 < j:
        solution = data[i:j]
        print(max(solution) + min(solution))
        solved = True
    elif sum(data[i:j]) > 22477624:
        i += 1
    elif j < len(data):
        j += 1 
    else:
        solved = True
        print("error")
