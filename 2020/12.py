with open("data/data_12.txt", "r") as fp:
    data = fp.readlines()

east = 0
north = 0
direction_degrees = 0
data = [d.strip() for d in data]
data = [[d[0], int(d[1:])] for d in data]
for d in data:
    if d[0] == "N":
        north += d[1]
    elif d[0] == "S":
        north -= d[1]
    elif d[0] == "E":
        east += d[1]
    elif d[0] == "W":
        east -= d[1]
    elif d[0] == "L":
        direction_degrees = (direction_degrees - d[1])%360
    elif d[0] == "R":
        direction_degrees = (direction_degrees + d[1])%360
    elif d[0] == "F":
        if direction_degrees == 0:
            east += d[1]
        elif direction_degrees == 90:
            north -= d[1]
        elif direction_degrees == 180:
            east -= d[1]
        elif direction_degrees == 270:
            north += d[1]
print(f"Part 1: {abs(east)+abs(north)}")

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
    if d[0] == "N":
        waypoint[1] += d[1]
    elif d[0] == "S":
        waypoint[1] -= d[1]
    elif d[0] == "E":
        waypoint[0] += d[1]
    elif d[0] == "W":
        waypoint[0] -= d[1]
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