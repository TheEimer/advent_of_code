from copy import deepcopy


def is_index(r, c):
    return 0 <= r < R and 0 <= c < C


def direct_neighbours(r, c):
    return [[r-1, c], [r+1, c], [r, c-1], [r, c+1], [r-1, c-1], [r-1, c+1], [r+1, c-1], [r+1, c+1]]


def sight_neighbours(r, c):
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


with open("data/data_11.txt", "r") as fp:
    data = fp.readlines()

data = [d.strip() for d in data]
layout = deepcopy(data)
R = len(layout)
C = len(layout[0])
layout = list(map(list, layout))
done = False
while not done:
    new_layout = deepcopy(layout)
    for j in range(len(layout)):
        for i in range(len(layout[j])):
            adj = direct_neighbours(j, i)
            adj = [a for a in adj if is_index(a[0], a[1])]
            if layout[j][i] == 'L' and all([layout[a[0]][a[1]] != '#' for a in adj]):
                new_layout[j][i] = '#'    
            elif layout[j][i] == '#' and sum([layout[a[0]][a[1]] == '#' for a in adj]) > 3:
                new_layout[j][i] = 'L'
    if layout == new_layout:
        done = True
    layout = new_layout.copy()

print(f"Part 1: {sum([l.count('#') for l in layout])}")

data = [d.strip() for d in data]
layout = deepcopy(data)
layout = list(map(list, layout))
done = False
while not done:
    new_layout = deepcopy(layout)
    for j in range(len(layout)):
        for i in range(len(layout[j])):
            adj = sight_neighbours(j, i)
            adj = [a for a in adj if is_index(a[0], a[1])]
            if layout[j][i] == 'L' and all([layout[a[0]][a[1]] != '#' for a in adj]):
                new_layout[j][i] = '#'
            elif layout[j][i] == '#' and sum([layout[a[0]][a[1]] == '#' for a in adj]) > 4:
                new_layout[j][i] = 'L'
    if layout == new_layout:
        done = True
    layout = new_layout.copy()

print(f"Part 2: {sum([l.count('#') for l in layout])}")
