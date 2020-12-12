from copy import deepcopy

def is_index(r, c):
    return 0 <= r < R and 0 <= c < C

def neighbours(r, c):
    return [[r-1, c], [r+1, c], [r, c-1], [r, c+1], [r-1, c-1], [r-1, c+1], [r+1, c-1], [r+1, c+1]]

data = []
with open("/home/eimer/Dokumente/advent_of_code_2020/data_11.txt", "r") as fp:
    data = fp.readlines()

data = [d.strip() for d in data]
layout = data.copy()
R = len(layout)
C = len(layout[0])
layout = list(map(list, layout))
done = False
while not done:
    new_layout = deepcopy(layout)
    for j in range(len(layout)):
        for i in range(len(layout[j])):
            adj = neighbours(j, i)
            adj = [a for a in adj if is_index(a[0], a[1])]
            if layout[j][i] == 'L' and all([layout[a[0]][a[1]] != '#' for a in adj]):
                new_layout[j][i] = '#'    
            elif layout[j][i] == '#' and sum([layout[a[0]][a[1]] == '#' for a in adj]) > 3:
                new_layout[j][i] = 'L'
    if layout == new_layout:
        done = True
    layout = new_layout.copy()

print(sum([l.count('#') for l in layout]))
