from itertools import permutations

path = "day_11.txt"
# path = "test.txt"

with open(path, 'r') as file:
    grid = [[c for c in line.strip()] for line in file]
    
# lets expand SPACE!
max_col = len(grid[0])
max_row = len(grid)
galaxies = [(i,j) for i in range(max_row) for j in range(max_col) if grid[i][j] == '#']
columns = [[line[j] for line in grid] for j in range(max_col)]
col_has_galaxy = [any(e != '.' for e in col) for col in columns]
line_has_galaxy = [any(e != '.' for e in line) for line in grid]
expansion_factor = 1_000_000

# print(col_has_galaxy)
for i,glxy in enumerate(galaxies):
    col_expansion = col_has_galaxy[0:glxy[1]].count(False) * (expansion_factor - 1)
    row_expansion = line_has_galaxy[0:glxy[0]].count(False) * (expansion_factor - 1)

    galaxies[i] = (glxy[0] + row_expansion, glxy[1] + col_expansion)

    # print(glxy, galaxies[i], sep=" --- ")

# print(galaxies)

distances = 0
for g1,g2 in set(permutations(galaxies, 2)):
    distances += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

print(distances//2)

# for i,line in enumerate(expanded):
#     print("\n", end='')
#     for j,c in enumerate(line):
#         print(c, end='')

# print("\n", end='')
