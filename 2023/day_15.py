from collections import defaultdict


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

answer = sum([my_hash(s) for s in seq])
print(answer)