from collections import deque
import heapq

path = "day_21.txt"
# path = "test.txt"

directions = {
    'l': (0, -1),
    'd': (1, 0),
    'r': (0, 1),
    'u': (-1, 0)
}


def start(grid):
    for i, line in enumerate(grid):
        if 'S' in line:
            return i, line.index('S')
    return -1


with open(path, 'r') as file:
    grid = [[c for c in line.strip()] for line in file]

STEP_LIMIT = 64
R = len(grid)
C = len(grid[0])
s = start(grid)

seen = set()

nodes = {}
# Dijkstra
q = [(0,s)]
while len(q) > 0:
    cost, coord = heapq.heappop(q)

    if coord in seen:
        continue
    
    if cost > STEP_LIMIT:
        continue

    seen.add(coord)
    nodes[coord] = cost

    for x,y in directions.values():
        i, j = coord
        new_i = i + x
        new_j = j + y

        if 0 <= new_i < R and 0 <= new_j < C and grid[new_i][new_j] != '#':
            heapq.heappush(q,(cost+1, (new_i, new_j)))

print(sum(1 for i in nodes if nodes[i]%2 == 0))

def draw(grid):
    for i,line in enumerate(grid):
        print("\n", end='')
        for j,c in enumerate(line):
            if (i,j) == s:
                print('S', end='')
            elif (i,j) in nodes and nodes[(i,j)]%2 == 0:
                print('O', end='')
            else:
                print(c, end='')
    print("\n", end='')

draw(grid)
# print(grid)