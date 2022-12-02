import numpy as np

with open('data/data_1.txt', 'r') as f:
    text = f.read().strip().split("\n\n")
calories = [sum(map(int, t.split())) for t in text]
max_elf, elf2, elf3 = np.argsort(calories)[::-1][:3]
max_calories, calories2, calories3 = calories[max_elf], calories[elf2], calories[elf3]
top_three_total = max_calories + calories2 + calories3
print(f'Elf {max_elf} carries the most calories with {max_calories} calories.')
print(f'Next in line are elf {elf2} and elf {elf3} with {calories2} and {calories3} calories respectively.')
print(f'In total these three elves carry {top_three_total} calories.')