import heapq


path = "day_17.txt"
# path = "test.txt"
grid = []
dist = {}

BFN = 2**64 - 1
with open(path, 'r') as file:
    grid = [[int(c) for c in line.strip()] for line in file]

R = len(grid)
C = len(grid)

directions = {
    'l': (0,-1),
    'd': (1,0),
    'r': (0, 1),
    'u': (-1,0)
}
possible = {
    'l': 'udl',
    'd': 'rld',
    'r': 'udr',
    'u': 'rlu'
}


def get_vertices(current, direction, straight_count):
    p = [d for d in possible[direction]]

    if straight_count < 4:
        p = [direction]
    if straight_count >= 10:
        p.pop()
    
    valid_vertices = []
    for d in p:
        x,y = directions[d]
        if 0 <= current[0]+x < R and 0 <= current[1]+y < C:
            valid_vertices.append(d)
        
    return valid_vertices

def draw(path, grid):
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    for i,line in enumerate(grid):
        print("\n", end='')

        for j,c in enumerate(line):
            if (i,j) in path:
                print(f'{OKGREEN}#{ENDC}', end='')
            else:
                print(c, end='')
    
    print()

seen = set()
q = [(0, (0,0), 'r', 0, [])]
answer = -1
hlpath = []
while len(q) > 0:
    cost, current, direction, straight_count, path = heapq.heappop(q)
    # print(cost, sep='\n', end='')
    # draw(path, grid)
    if (current, direction, straight_count) in seen:
        continue

    seen.add((current, direction, straight_count))

    if current == (R-1, C-1):
        answer = cost
        hlpath = path
        break

    for dir in get_vertices(current, direction, straight_count):
        nxt_coord = (directions[dir][0] + current[0], directions[dir][1] + current[1])
        nxt_path = path + [(nxt_coord)]
        if nxt_coord in seen:
            continue

        distance = cost + grid[nxt_coord[0]][nxt_coord[1]]
        if dir == direction:
            heapq.heappush(q,(distance, nxt_coord, dir, straight_count + 1, nxt_path))
        else:
            heapq.heappush(q,(distance, nxt_coord, dir, 1, nxt_path))

draw(hlpath, grid)
print(answer)

    
