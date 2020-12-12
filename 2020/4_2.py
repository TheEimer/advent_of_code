data = []
with open("/home/eimer/Dokumente/advent_of_code_2020/data_4.txt", "r") as fp:
    data = fp.readlines()

passports = {}
passports["0"] = {}
count = 0
new_passport = False
for i in range(len(data)):
    if not data[i].strip():
        new_passport = True
        continue
    if new_passport:
        new_passport = False
        count += 1
        passports[f"{count}"] = {}
    line = data[i].strip().split(" ")
    for l in line:
        pair = l.split(":")
        passports[f"{count}"][pair[0]] = pair[1]

valid = 0
features = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
for k in passports.keys():
    if all(f in passports[k].keys() for f in features):
        conditions = []
        conditions.append(int(passports[k]["byr"]) <= 2020 and int(passports[k]["byr"]) >= 1920)
        conditions.append(int(passports[k]["iyr"]) <= 2020 and int(passports[k]["iyr"]) >= 2010)
        conditions.append(int(passports[k]["eyr"]) <= 2030 and int(passports[k]["eyr"]) >= 2020)
        height_inch = passports[k]["hgt"][-2:] == "in" and int(passports[k]["hgt"][:-2]) <= 76 and int(passports[k]["hgt"][:-2]) >= 59
        height_cm = passports[k]["hgt"][-2:] == "cm" and int(passports[k]["hgt"][:-2]) <= 193 and int(passports[k]["hgt"][:-2]) >= 150
        conditions.append(height_cm or height_inch)
        hair_color_characters = all([passports[k]["hcl"][i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"] for i in range(1, len(passports[k]["hcl"]))])
        conditions.append(passports[k]["hcl"][0] == "#" and len(passports[k]["hcl"][1:]) == 6 and hair_color_characters)
        conditions.append(passports[k]["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
        conditions.append(len(passports[k]["pid"]) == 9)

        if all(conditions):
            valid += 1
print(valid)
