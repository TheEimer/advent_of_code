data = []
with open("/home/eimer/Dokumente/advent_of_code_2020/data_5.txt", "r") as fp:
    data = fp.readlines()

ids = []
for i in range(len(data)):
    rep = data[i].strip()
    max_row = 127
    min_row = 0
    for j in range(7):
        if rep[j] == "B":
            min_row += (max_row-min_row)//2+1
        else:
            max_row -= (max_row-min_row)//2+1
    max_col = 7
    min_col = 0
    for j in range(3):
        if rep[j+7] == "R":
            min_col += (max_col-min_col)//2+1
        else:
            max_col -= (max_col-min_col)//2+1
    seat_id = 8*min_row + min_col
    ids.append(seat_id)

missing_seats = []

for i in range(128*8):
    if i not in ids:
        row = i//8
        col = i%8
        if row > 7 and row < 117:
            missing_seats.append([row, col])
print(missing_seats)
print(missing_seats[0][0]*8 + missing_seats[0][1])
