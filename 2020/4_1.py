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
        valid += 1
print(valid)
