from itertools import cycle
from math import lcm

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
# current = 'AAA'
counter = 0
i_len = len(instructions)
instructions = cycle(instructions)
cycles = {}

for c in current:
    cycle_detected = False
    z_node = None
    state = {}
    origin = c

    # this is the shittiest cycle detection possible
    # but I've verified that all the A nodes have only one Z node per cycle
    while not cycle_detected:
        i_index = counter % i_len
        i = next(instructions)
        c = nodes[c][i]
        counter += 1

        if c.endswith('Z'):
            if z_node == None:
                z_node = c
                state[c] = (i_index, counter)
            elif state[c][0] == i_index:
                cycle_detected = True
                cycles[c] = counter - state[c][1]


print(lcm(*cycles.values()))
# By the way, the brute force solution is still running
# I guess it will kinda run forever if I let
# Based on the fact that the sollution is on the 10^13 order
