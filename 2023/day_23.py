from collections import defaultdict, deque

path = "day_23.txt"
# path = "test.txt"

directions = {
    'l': (0, -1),
    'd': (1, 0),
    'r': (0, 1),
    'u': (-1, 0)
}

slopes = {
    '<': (0, -1),
    'v': (1, 0),
    '>': (0, 1),
    '^': (-1, 0)
}

def get_neighboors(coord, grid):
    r,c = coord
    R = len(grid)
    C = len(grid[0])
    n = []
    for i,j in directions.values():
        nxt_r = r+i
        nxt_c = c+j
        if 0 <= nxt_r < R and 0 <= nxt_c < C and grid[nxt_r][nxt_c] != '#':
            n.append((nxt_r, nxt_c))

    return n

# thanks to https://github.com/janek37/advent-of-code/blob/main/2023/day23.py
# My graph skills kinda suck
def build_graph(grid):
    g = {}
    s = deque([(0, grid[0].index('.'))])

    while s:
        r,c = s.pop()
        if (r,c) in g:
            continue

        g[(r,c)] = []
        for nxt_r,nxt_c in get_neighboors((r,c), grid):
            prev = (r,c)
            distance = 1
            while True:
                n = [x for x in get_neighboors((nxt_r, nxt_c), grid) if x != prev]

                if len(n) != 1:
                    break

                prev = (nxt_r, nxt_c)
                nxt_r, nxt_c = n[0]
                distance += 1

            g[(r,c)].append((nxt_r, nxt_c, distance))
            s.append((nxt_r, nxt_c))

    return g


def dfs(graph, start, goal):
    s = [(start, 0, {start})]
    distances = defaultdict(int)

    while s:
        current, distance, visited = s.pop()
        
        distances[current] = max(distances[current], distance)
        
        for r,c,d in graph[current]:
            if (r,c) in visited or current == goal:
                continue
            s.append(((r,c), distance + d, visited | {(r,c)}))

    return distances


with open(path, 'r') as file:
    grid = [[c if c not in slopes else '.' for c in line.strip() ] for line in file]


R = len(grid)
C = len(grid[0])
start = (0,1)
goal = (R-1, grid[R-1].index('.'))
print(dfs(build_graph(grid), start, goal)[goal])
