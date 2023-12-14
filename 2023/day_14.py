from copy import deepcopy

path = "day_14.txt"
# path = "test.txt"

def rotate_90(grid):
    return [[grid[i][j] for i in range(len(grid) - 1, -1, -1)] for j in range(len(grid[0]))]

with open(path, 'r') as file:
    grid = [[c for c in line.strip()] for line in file]

r = len(grid)
c = len(grid[0])

def cycle(grid):
    for _ in range(4):
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 'O':
                    for k in range(1, i + 1):
                        if grid[i - k][j] != '.':
                            break
                        grid[i - k][j] = 'O'
                        grid[i - k + 1][j] = '.'

        grid = rotate_90(grid)

    return grid


def draw(grid):
    for i,line in enumerate(grid):
        print("\n", end='')
        for j,c in enumerate(line):
            print(c, end='')
    print("\n", end='')

def hash_grid(grid):
    return hash(''.join([c for line in grid for c in line]))

cycle_detected = False
state = {}
counter = 0
cycle_size = 2**32
cycle_start = 0
grid_hash = hash_grid(grid)
while not cycle_detected:
    state[grid_hash] = counter
    grid = cycle(grid)
    grid_hash = hash_grid(grid)
    counter += 1

    if grid_hash in state:
        cycle_start = state[grid_hash]
        cycle_size = counter - state[grid_hash]
        cycle_detected = True

total_cycles = 1_000_000_000

for _ in range((total_cycles - cycle_start)%cycle_size):
    grid = cycle(grid)

# draw(grid)
print(f'Cycle size: {cycle_size}, Cycle_start: {cycle_start}')
answer = [len(grid)-i for j in range(c) for i in range(r) if grid[i][j] == 'O']
print(sum(answer))
