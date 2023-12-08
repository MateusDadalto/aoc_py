from itertools import cycle

path = "day_8.txt"
# path = "test.txt"

with open(path, 'r') as file:
    f  = file.read()

instructions, n = f.split('\n\n')

nodes = {}
for node in n.split('\n'):
    name = node[0:3]
    left = node[7:10]
    right = node[12:15]
    nodes[name] = {'R': right, 'L': left}

current: list[str] = [a for a in nodes.keys() if a.endswith('A')]
counter = 0
instructions = cycle(instructions)
while(not all(z.endswith('Z') for z in current)):
    i = next(instructions)
    current = [nodes[c][i] for c in current]
    counter += 1

print(counter)