from collections import defaultdict
from collections import deque

path = "day_24.txt"
path = "test.txt"

with open(path) as f:
    inpt = [section for section in f.read().split('\n\n')]
    first_section = [i.strip() for i in inpt[0].splitlines()]
    second_section = [i.strip() for i in inpt[1].splitlines()]
    
# print(first_section)
# print(second_section)

def run_op(g1: bool, op: str, g2: bool):
    if op == 'AND':
        return g1 and g2
    
    if op == 'XOR':
        return g1 ^ g2
    
    if op == 'OR':
        return g1 or g2
        

gates = deque([])

values = defaultdict()

for line in first_section:
    key = line[0:3]
    value = int(line[-1]) == 1
    
    values[key] = value
    
for line in second_section:
    g1, op, g2, _, dest = line.split()
    
    gates.append((g1, op, g2, dest))
    
results = []
while (len(gates)) > 0:
    g1, op, g2, dest = gates.popleft()
    
    if g1 not in values or g2 not in values:
        gates.append((g1, op, g2, dest))
        continue
    
    r = run_op(values[g1], op, values[g2])
    
    values[dest] = r
    if dest.startswith('z'):
        results.append(dest)

results = sorted(results)  
print(results)

print(sum([values[key] << i for i,key in enumerate(results)]))