def get_score(signs):
    score = (ord(signs[0]) - ord(signs[1]) + 23) % 3
    return (-score+1)*3 if score==0 or score==1 else 6

def get_shape(inputs):
    return (ord(inputs[0])-87+22 -ord('Y') + ord(inputs[1])) % 3+1

with open('data/data_2.txt', 'r') as f:
    text = f.read().strip().split("\n")
    
scores = [ord(a.split()[1])-87+get_score(a.split()) for a in text]
print(f'The total score according to the test guide would be {sum(scores)}')
scores2 = [get_shape(a.split())+3*(ord(a.split()[1])-88) for a in text]
print(f'The total score according to the test guide when used correctly would be {sum(scores2)}')