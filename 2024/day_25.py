from collections import defaultdict
from collections import deque

path = "day_25.txt"
# path = "test.txt"

with open(path) as f:
    inpt = [section for section in f.read().split('\n\n')]
    grids = [[l.strip() for l in s.splitlines()] for s in inpt]
    
    
def extract_heights(grid, is_lock):
    heights = []
    for col in range(len(grid[0])):
        max_height = 0
        for row in range(len(grid)):
            if grid[row][col] == '#' and is_lock:
                max_height = row
            
            if grid[row][col] == '.' and not is_lock:
                max_height = (len(grid) - 1) - (row + 1)

        heights.append(max_height)
    
    return heights

def matches(lock, key, height):
    return all([l+k < height for l,k in zip(lock, key)])

keys = []
locks = []
for g in grids:
    is_lock = g[0][0] == '#'
    r = extract_heights(g, is_lock)
    locks.append(r) if is_lock else keys.append(r)
    
height = len(g) - 1

p1 = 0
for lock in locks:
    match = [k for k in keys if matches(lock, k, height)]
    # print(lock, 'matches', match)
    p1 += len(match)

print(p1)