from copy import deepcopy

def is_index(r, c):
    return 0 <= r < R and 0 <= c < C

def neighbours(r, c):
    neigh = []
    for row in [-1, 0, 1]:
        for column in [-1, 0, 1]:
            if row == column and row == 0:
                continue
            for count in range(1, len(layout)):
                if is_index(r + count*row, c + count*column):
                    if layout[r + count*row][c + count*column] != '.':
                        neigh.append([r + count*row, c + count*column])
                        break
                count += 1
    return neigh

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
            elif layout[j][i] == '#' and sum([layout[a[0]][a[1]] == '#' for a in adj]) > 4:
                new_layout[j][i] = 'L'
    if layout == new_layout:
        done = True
    layout = new_layout.copy()

print(sum([l.count('#') for l in layout]))
