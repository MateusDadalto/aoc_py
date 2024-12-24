from collections import defaultdict
from collections import deque
import graphviz

path = "day_24.txt"
# path = "test.txt"

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

values = {}
initial_values = {}
graph = {}
x = []
y = []
gviz = graphviz.Digraph(name="t2")

for line in second_section:
    g1, op, g2, _, dest = line.split()
    
    gates.append((g1, op, g2, dest))
    graph[dest] = (g1, op, g2)
    gviz.edge(dest, g1, label=op)
    gviz.edge(dest, g2, label=op)

for line in first_section:
    key = line[0:3]
    value = int(line[-1]) == 1
    
    values[key] = value
    initial_values[key] = value
    if key.startswith('x'):
        x.append(key)
    if key.startswith('y'):
        y.append(key)
        
    


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
# print(results)
sum_z = sum([values[key] << i for i,key in enumerate(results)])
sum_x = sum([values[key] << i for i,key in enumerate(sorted(x))])
sum_y = sum([values[key] << i for i,key in enumerate(sorted(y))])
print('p1:', sum_z)
print('x:', sum_x)
print('y:', sum_y)
print('x+y:', sum_y + sum_x)
print('binxy:', bin((sum_y + sum_x)))
print('bin z:', bin(sum_z))
print('bin d:', f'{(sum_y + sum_x) ^ sum_z:#048b}')
    
def test(node:str, graph, initial_values):
    if node in initial_values:
        print(node, '->', initial_values[node])
        return
    
    print(node, '->', graph[node])
    g1, _, g2 = graph[node]
    test(g1, graph, initial_values)
    test(g2, graph, initial_values)

    
for dest in values:
    gviz.node(dest, label=f'{dest} - {int(values[dest])}')

# From here ownwards it was Ripple Carry Adder visual analysis (thanks reddit)
gviz.render(directory='./')
