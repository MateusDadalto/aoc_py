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
    # grid = [[c for c in line.strip()] for line in file]
    grid = [[c for c in line.strip()] *7 for line in file] *7

STEP_LIMIT = 64
R = len(grid)
C = len(grid[0])
s = start(grid)
s = (s[0] *7 + 3, s[1]*7 + 3)

def dijkstra(grid, start, distance):

    seen = set()
    nodes = {}
    # Dijkstra
    q = [(0,start)]
    while len(q) > 0:
        cost, coord = heapq.heappop(q)

        if coord in seen:
            continue

        if distance and cost > distance:
            continue

        seen.add(coord)
        nodes[coord] = cost

        for x,y in directions.values():
            i, j = coord
            new_i = i + x
            new_j = j + y

            if 0 <= new_i < R and 0 <= new_j < C and grid[new_i][new_j] != '#':
                heapq.heappush(q,(cost+1, (new_i, new_j)))
    
    return nodes

nodes = dijkstra(grid, s, None)
## part 1
print(sum(1 for i in nodes if nodes[i] <= 64 and nodes[i]%2 == 0))
# I could not figure out this problem, My head is buzzing with grids and steps
# got this solution from https://github.com/thomasjevskij/advent_of_code/blob/master/2023/aoc21/day21.py
fs = []
for n in range(0, 3):
    fs.append(sum(1 for i in nodes if nodes[i]%2 != n%2 and nodes[i] <= (65+131*n)))
    # print(even)

f0,f1,f2 = fs
# print(f0, f1, f2)

c = f0
a = (f2 - 2*f1 + f0) // 2 # Don't worry this is an integer :-)
b = f1 - f0 - a
f = lambda n: a*n**2 + b*n + c
N = (26501365 - 65) // 131
print(f(N))
