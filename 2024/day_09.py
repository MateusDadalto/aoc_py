from itertools import cycle
from collections import deque
path = "day_09.txt"
# path = "test.txt"

with open(path) as f:
    line = f.readline()


loop = cycle(['F', '.'])
blocks = []
id = 0
for c in line:
    f_or_dot = next(loop)
    blocks += [id]*int(c) if f_or_dot == 'F' else [-1]*int(c)
    
    id += 1 if f_or_dot == 'F' else 0

SIZE = len(blocks)
q = deque(blocks)

# compress
compressed = []
fill_empty = False
while len(q) > 0:
    if fill_empty:
        digit = q.pop()
    else:
        digit = q.popleft()
    
    if digit < 0:
        fill_empty = True
    else:
        compressed.append(digit)
        fill_empty = False
    

# print(compressed)
p1 = sum([i*compressed[i] for i in range(len(compressed))])

print(p1)
