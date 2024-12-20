import heapq
from collections import Counter

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

path = dijkstra(grid, start)

jumps = []
total = 0
for node in path:
    for d in directions:
        leap_end = node + d*2
        if is_valid(leap_end, grid) and not is_valid(node + d, grid):
            # minus 2 to to discount their own node time
            leap_size = path[leap_end] - path[node] - 2
            
            if leap_size >= 100:
                jumps.append(leap_size)
                total += 1

# print(Counter(jumps))
print(total)

