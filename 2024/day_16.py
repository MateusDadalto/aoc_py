import cmath
from collections import deque
from time import sleep
from typing import Deque, Tuple, Dict, List
from copy import deepcopy

# Let's try complex numbers

path = "day_16.txt"
path = "test.txt"

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

# If you want to print something...
def print_grid(grid, path, pos, d, label, slp):
    print_d = {complex(0,1): '>', complex(1,0): 'v', complex(-1,0): '^', complex(0,-1): '<'}
    v = set(path)
    for r in range(len(grid)):
        print()
        for c in range(len(grid[0])):
            current = complex(r,c)
            
            if current == pos:
                print(print_d[d], end='')
            elif current in v:
                print("0", end="")
            else:
                print(grid[r][c], end="")
                
    print()
    print('='*len(grid[0]))
    print(label)
    sleep(slp)
    
    
while len(q) > 0:
    pos, d, score, turned, visited, path = q.popleft()

    if (pos, d) in visited and visited[(pos,d)] < score:
        print_grid(grid, path, pos, d, 'ALREADY VISITED W/ LOWER SCORE', 1)
        continue
    
    visited[(pos,d)] = score
    path = [pos] + path
    if score > min_score:
        print_grid(grid, path, pos, d, 'ALREADY FOUND A COMPLETE PATH WITH LOWER SCORE', 1)
        continue
    
    new_pos = pos + d
    
    if is_end(new_pos, grid):
        if score + 1 == min_score:
            best_path.update(path)
            print_grid(grid, path, pos, d, 'NEW EQUALLY GOOD PATH', 1)
            continue
        
        if score <= min_score:
            min_score = min(min_score, score + 1)
            print_grid(grid, path, pos, d, 'NEW BEST PATH', 1)

            best_path.clear()
            best_path.update(path)
            best_path.add(new_pos)
            
        continue
    
    print_grid(grid, path, pos, d, 'WALKING', 0.2)
    
    if not turned:
        q.append((pos, d*turn_clockwise, score + 1000, True, visited, path))
        q.append((pos, d*turn_ctrclockwise, score + 1000, True, visited, path))
    
    if is_valid(new_pos, grid):
        q.append((new_pos, d, score + 1, False, visited, path))
        
    
print("p1:",min_score)
print("p2:", len(best_path))

