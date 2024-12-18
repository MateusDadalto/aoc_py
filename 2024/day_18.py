import cmath
from collections import deque
import heapq
from typing import Deque, Tuple, Dict, List
from copy import deepcopy

# Let's try complex numbers

path = "day_18.txt"
# path = "test.txt"

with open(path) as f:
    lines = [l.strip().split(',') for l in f.readlines()]
    
def is_inside(pos:complex, rows, cols):
    r = int(pos.real)
    c = int(pos.imag)
    
    return 0 <= r < rows and 0<= c < cols

def is_fallen(pos, fallen, nanos):
    return pos in fallen and  nanos > fallen[pos]

def is_end(pos:complex, rows, cols):
    
    return pos == complex(rows-1, cols-1)

# If you want to print something...
def print_grid(rows, cols, current, visited, nanos, fallen):
    print()
    print('='*cols)
    print()
    print(f'nanos: {nanos}')
    
    
    for r in range(rows):
        print()
        for c in range(cols):
            pos = complex(r, c)
            if pos == current:
                print('&', end='')
            elif pos in visited:
                print("0", end="")
            elif pos in fallen and nanos > fallen[pos]:
                print('#', end="")
            else:
                print('.', end='')
                
    print()
    print('='*cols)
    print()
    

# Attention, input is inverted, first is COLS then ROWS
falling_bytes = [complex(int(l[1].strip()), int(l[0].strip())) for l in lines]

# print(falling_bytes)
initial_falling_nanos = 2**10
ROWS = 71
COLS = 71

# initial_falling_nanos = 12
# ROWS = 7
# COLS = 7

initial_pos = complex(0,0)
goal = complex(ROWS, COLS)

fall = {tile: nanos for nanos, tile in enumerate(falling_bytes)}
directions = (complex(1,0), complex(0,1), complex(0,-1), complex(-1,0))


# copied from my own 2023 day 21 solution. I never remember Dijkstra
def dijkstra(fallen, start: complex, nanos):

    seen = set()
    nodes = {}
    # Dijkstra
    q = [(0,(start.real, start.imag))]
    while len(q) > 0:
        steps, coord = heapq.heappop(q)

        if coord in seen:
            continue

        seen.add(coord)
        nodes[coord] = steps
        pos = complex(coord[0], coord[1])

        for d in directions:
            new_pos = pos + d

            if is_inside(new_pos, ROWS, COLS) and not is_fallen(new_pos, fallen, nanos):
                heapq.heappush(q,(steps+1, (int(new_pos.real), int(new_pos.imag))))
    
    return nodes

nodes = dijkstra(fall, initial_pos, initial_falling_nanos)

print(nodes)
print(nodes[(70,70)])

def can_flood_fill_till_end(fallen, initial_pos: complex, nanos, rows, cols):
    steps = deque([initial_pos])
    visited = set()
    a = 0
    while len(steps) > 0:
        a += 1
        pos = steps.popleft()
        visited.add(pos)
        if is_end(pos, ROWS, COLS):
            
            return True
        
        for d in directions:
            new_pos = pos + d
            if new_pos in visited:
                continue
            
            if (not is_inside(new_pos, rows, cols)) \
                or is_fallen(new_pos, fallen, nanos) \
                or new_pos in visited:
                continue
            
            steps.appendleft(new_pos)
    
    print_grid(ROWS, COLS, pos, visited, nanos, fallen)
    return False



for i in range(initial_falling_nanos, len(falling_bytes)):
    
    total =  len(falling_bytes) - initial_falling_nanos
    
    if not can_flood_fill_till_end(fall, complex(0,0), i, ROWS, COLS):
        # N-1 IN THE INDEX MISTAKEEEEE 1 HOUR ON THIS F*
        print(f'p1: {i}', falling_bytes[i-1], sep= ' -> ')
        break
    
    percentage = (i-initial_falling_nanos)/total * 100
    print(f'{percentage:.2f}%', end='\r')