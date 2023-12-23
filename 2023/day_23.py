from collections import defaultdict, deque


path = "day_23.txt"
# path = "test.txt"

    
def draw_step(current, grid):
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    for i,line in enumerate(grid):
        print("\n", end='')

        for j,c in enumerate(line):
            if (i,j) == current:
                print(f'{OKGREEN}X{ENDC}', end='')
            else:
                print(c, end='')
    
    print()    

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


def dfs(grid):
    s = deque([(0, grid[0].index('.'), 0, (-1, 0))])
    seen = defaultdict(int)
    R = len(grid)
    C = len(grid[0])

    while len(s) > 0:
        r,c, steps, prev = s.popleft()
        seen[(r,c)] = steps
        # draw((r,c), grid)
        for i,j in directions.values():
            nxt_r = r+i
            nxt_c = c+j
            nxt_step = steps + 1
            if 0 <= nxt_r < R and 0 <= nxt_c < C and \
                grid[nxt_r][nxt_c] != '#' and (nxt_r,nxt_c) != prev:
                char = grid[nxt_r][nxt_c]
                if char in slopes and \
                    (r,c) == (slopes[char][0] + nxt_r, slopes[char][1] + nxt_c):
                    continue
                elif char in slopes:
                    if seen[(nxt_r, nxt_c)] > nxt_step:
                        continue
                    seen[(nxt_r, nxt_c)] = nxt_step
                    
                    s.appendleft((nxt_r + slopes[char][0], nxt_c + slopes[char][1], nxt_step + 1, (nxt_r, nxt_c)))
                    continue
                
                s.appendleft((nxt_r, nxt_c, nxt_step, (r,c)))

    return seen


with open(path, 'r') as file:
    grid = [[c for c in line.strip()] for line in file]


R = len(grid)
C = len(grid[0])

# debug stuff
# def draw(current, grid):
#     OKGREEN = '\033[92m'
#     ENDC = '\033[0m'
#     for i,line in enumerate(grid):
#         print("\n", end='')

#         for j,c in enumerate(line):
#             if (i,j) in current:
#                 print(current[(i,j)], end='\t')
#             else:
#                 print(c, end='\t')
    
#     print()


# draw(dfs(grid), grid)

distances = dfs(grid)

print(distances[(R-1, grid[R-1].index('.'))])