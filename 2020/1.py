with open("data/data_1.txt", "r") as fp:
    data = fp.readlines()
data = [int(d) for d in data]

for i in data:
    for j in data:
        if i!=j and i+j==2020:
            print(f"Part 1: {i*j}")
            break

for i in data:
    for j in data:
        for k in data:
            if i!=j and i!=k and k!=j and i+j+k==2020:
                print(f"Part 2: {i*j*k}")
                break
