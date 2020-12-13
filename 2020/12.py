with open("data/data_12.txt", "r") as fp:
    data = fp.readlines()

directions = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
changes = {"N": ("W", "E"), "S": ("E", "W"), "E": ("N", "S"), "W": ("S", "N")}

position = [0, 0]
direction = "E"
data = [d.strip() for d in data]
data = [[d[0], int(d[1:])] for d in data]
for d in data:
    if d[0] in directions.keys():
        position[0] += directions[d[0]][0] * d[1]
        position[1] += directions[d[0]][1] * d[1]
    elif d[0] == "L":
        for i in range(d[1]//90):
            direction = changes[direction][0]
    elif d[0] == "R":
        for i in range(d[1]//90):
            direction = changes[direction][1]
    elif d[0] == "F":
        position[0] += directions[direction][0] * d[1]
        position[1] += directions[direction][1] * d[1]

print(f"Part 1: {abs(position[0])+abs(position[1])}")

def turn_right(w):
    if w[0] < 0:
        north = abs(w[0])
        east = w[1]
    else:
        north = -w[0]
        east = w[1]
    return [east, north]

def turn_left(w):
    if w[1] < 0:
        north = w[0]
        east = abs(w[1])
    else:
        north = w[0]
        east = -w[1]
    return [east, north]

waypoint = [10, 1]
position = [0, 0]
for d in data:
    if d[0] in directions.keys():
        waypoint[0] += directions[d[0]][0] * d[1]
        waypoint[1] += directions[d[0]][1] * d[1]
    elif d[0] == "L":
        for _ in range(d[1]//90):
            waypoint = turn_left(waypoint)
    elif d[0] == "R":
        for _ in range(d[1]//90):
            waypoint = turn_right(waypoint)
    elif d[0] == "F":
        position[0] += waypoint[0]*d[1]
        position[1] += waypoint[1]*d[1]
print(f"Part 2: {abs(position[0])+abs(position[1])}")