from collections import deque
from functools import cache
import networkx as nx

path = "day_23.txt"
# path = "test.txt"

with open(path) as f:
    connections = [l.strip() for l in f.readlines()]

graph = nx.Graph()

for c in connections:
    pc1, pc2 = c.split('-')
    graph.add_edge(pc1,pc2)

print(','.join(sorted(max([i for i in nx.find_cliques(graph)], key=len))))
