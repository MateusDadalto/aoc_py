from collections import OrderedDict


path = "day_15.txt"
# path = "test.txt"

with open(path, 'r') as file:
    seq = file.readline()[:-1].split(',')
    # print(seq)

def my_hash(s: str):
    current = 0
    for c in s:
        current += ord(c)
        current *= 17
        current = current%256
    
    return current

boxes = [OrderedDict() for _ in range(256)]
for s in seq:
    label = ''
    i = 0
    while s[i].isalpha():
        label += s[i]
        i += 1
    
    symbol = s[i]
    box = my_hash(label)

    if symbol == '-' and label in boxes[box]:
        boxes[box].pop(label)
    elif symbol == '=':
        number = int(s[-1])
        boxes[box][label] = number
    
    
answer = [(i, b) for i,b in enumerate(boxes) if len(b.keys()) > 0]
sum = 0
for i,b in answer:
    for j, lens in enumerate(b.values()):
        sum += (i+1) * (j+1) * lens
# answer = sum([my_hash(s) for s in seq])
print(sum)