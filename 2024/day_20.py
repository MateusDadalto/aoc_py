from functools import cache
import heapq
from collections import Counter
from types import MappingProxyType
from typing import Dict

path = "day_20.txt"
# path = "test.txt"

directions = (complex(1,0), complex(0,1), complex(0,-1), complex(-1,0))

with open(path) as f:
    grid = [l.strip() for l in f.readlines()]
    
ROWS = len(grid)
COLS = len(grid[0])

for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == 'S':
            start = complex(r,c)
        elif grid[r][c] == 'E':
            end = complex(r,c)

def is_valid(pos:complex, grid):
    r = int(pos.real)
    c = int(pos.imag)
    rows = len(grid)
    cols = len(grid[0])
    
    return 0 <= r < rows and 0<= c < cols and grid[r][c] != '#'
    
def dijkstra(grid, start: complex): 

    seen = set()
    nodes = {}
    # Dijkstra
    q = [(0, (int(start.real), int(start.imag)))]
    while len(q) > 0:
        steps, coord = heapq.heappop(q)

        if coord in seen:
            continue

        seen.add(coord)
        pos = complex(coord[0], coord[1])
        nodes[pos] = steps

        for d in directions:
            new_pos = pos + d

            if is_valid(new_pos, grid):
                heapq.heappush(q,(steps+1, (int(new_pos.real), int(new_pos.imag))))
    
    return nodes

path: Dict[complex, int] = dijkstra(grid, start)

jumps = []
total = 0
for node in path:
    for d in directions:
        leap_end = node + d*2
        if is_valid(leap_end, grid) and not is_valid(node + d, grid):
            # the distance between them - 2 to account the steps
            leap_size = path[leap_end] - path[node] - 2
            
            if leap_size >= 100:
                jumps.append(leap_size)
                total += 1

# print(Counter(jumps))
print(total)
# print(path.keys())
# p2

# since python dict since 3.7 maintain order of insertion
p2_jumps = []
p2 = 0
keys = [k for k in path.keys()]
for i in range(len(keys)):
    node1 = keys[i]
    for j in range(i, len(keys)):
        node2 = keys[j]
        grid_distance = node2 - node1
        # taxicab distance
        tb_distance = abs(grid_distance.real) + abs(grid_distance.imag)
        path_distance = path[node2] - path[node1]
        
        if 0 < tb_distance <= 20 and tb_distance < path_distance:
            leap_size = int(path_distance - tb_distance)
            
            if leap_size >= 100:
                p2_jumps.append(leap_size)
                p2 += 1
    
    percentage = int(i/len(keys) *100)
    print(f'{percentage}%', end= '\r')

print(f'100%', end= '\r')

print(Counter(p2_jumps))
print(p2)