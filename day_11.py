from itertools import permutations

path = "day_11.txt"
# path = "test.txt"

EMPTY_SPACE = '.'

with open(path, 'r') as file:
    grid = [[c for c in line.strip()] for line in file]
    
# lets expand SPACE!
max_col = len(grid[0])
max_row = len(grid)

columns = [[line[j] for line in grid] for j in range(max_col)]
col_has_galaxy = [any(e != '.' for e in col) for col in columns]
line_has_galaxy = [any(e != '.' for e in line) for line in grid]
# print(line_has_galaxy)


expanded = []
for i in range(max_row):
    space = []
    for j in range(max_col):
        space.append(grid[i][j]) if col_has_galaxy[j] else space.extend([EMPTY_SPACE, EMPTY_SPACE])
    
    expanded.append(space) if line_has_galaxy[i] else expanded.extend([space, space])

max_col = len(expanded[0])
max_row = len(expanded)

galaxies = [(i,j) for j in range(max_col) for i in range(max_row) if expanded[i][j] == '#']
# print(galaxies)

distances = 0
for g1,g2 in set(permutations(galaxies, 2)):
    distances += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

print(distances/2)
# for i,line in enumerate(expanded):
#     print("\n", end='')
#     for j,c in enumerate(line):
#         print(c, end='')

# print("\n", end='')
