from collections import defaultdict
import networkx as nx

path = "day_25.txt"
# path = "test.txt"

g = nx.DiGraph()
with open(path, 'r') as file:
    for line in file:
        line = line.strip()
        node, con = line.split(':')
        for c in con.split():
            g.add_edge(node, c, capacity=1.0)
            g.add_edge(c, node, capacity=1.0)

nodes = [n for n in g]
# print(nodes)
for n2 in nodes[1:]:
    n = nodes[0]
    cut_value, partition = nx.minimum_cut(g, n, n2)
    if cut_value == 3:
        print(len(partition[0])*len(partition[1]))
        break
