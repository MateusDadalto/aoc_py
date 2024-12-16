import cmath
from collections import deque
from typing import Deque, Tuple, Dict, List
from copy import deepcopy

# Let's try complex numbers

path = "day_16.txt"
# path = "test.txt"

with open(path) as f:
    grid = [l.strip() for l in f.readlines()]

ROWS = len(grid)
COLS = len(grid[0])
start_direction = complex(0,1)
start_pos = complex(0, 0)
turn_clockwise = complex(0,1)
turn_ctrclockwise = complex(0,-1)

for row in range(ROWS):
    for col in range(COLS):
        if grid[row][col] == 'S':
            start_pos = complex(row, col)
            break
            
q: Deque[Tuple[complex, complex, int, bool, Dict, List]] = deque()
q.append((start_pos, start_direction, 0, False, {}, []))

def is_valid(pos:complex, grid):
    r = int(pos.real)
    c = int(pos.imag)
    rows = len(grid)
    cols = len(grid[0])
    
    return 0 <= r < rows and 0<= c < cols and grid[r][c] != '#'

def is_end(pos:complex, grid):
    r = int(pos.real)
    c = int(pos.imag)
    rows = len(grid)
    cols = len(grid[0])
    
    return 0 <= r < rows and 0<= c < cols and grid[r][c] == 'E'


min_score = 1_000_000_000_000_000
best_path = set()

while len(q) > 0:
    pos, d, score, turned, visited, path = q.popleft()

    if (pos, d) in visited and visited[(pos,d)] < score:
        continue

    visited[(pos,d)] = score
    path = [pos] + path
    if score > min_score:
        continue
    
    new_pos = pos + d
    
    if is_end(new_pos, grid):
        if score + 1 == min_score:
            best_path.update(path)
            continue
        
        if score <= min_score:
            min_score = min(min_score, score + 1)

            best_path.clear()
            best_path.update(path)
            best_path.add(new_pos)
            
        continue
            
    if not turned:
        q.append((pos, d*turn_clockwise, score + 1000, True, visited, path))
        q.append((pos, d*turn_ctrclockwise, score + 1000, True, visited, path))
    
    if is_valid(new_pos, grid):
        q.append((new_pos, d, score + 1, False, visited, path))
        
    
print("p1:",min_score)
print("p2:", len(best_path))

# If you want to print something...
def print_grid(grid, path):
    v = set(path)
    for r in range(len(grid)):
        print()
        for c in range(len(grid[0])):
            if complex(r, c) in v:
                print("0", end="")
            else:
                print(grid[r][c], end="")
                
    print()
    print('='*len(grid[0]))
    print()
    
