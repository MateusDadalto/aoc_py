path = "day_16.txt"
# path = "test.txt"

with open(path, 'r') as file:
    grid = [[c for c in line.strip()] for line in file]

beams = [(0, -1, 'R')]
R = len(grid)
C = len(grid)
directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'R': (0, 1),
    'L': (0, -1)
}
reflections = {
    'R': {'/': 'U', '\\': 'D'},
    'L': {'/': 'D', '\\': 'U'},
    'U': {'/': 'R', '\\': 'L'},
    'D': {'/': 'L', '\\': 'R'},
}


def beam_deflect(beam, i, j, char):
    if char == '-':
        return beam[2] if beam[2] in 'RL' else 'RL'

    if char == '|':
        return beam[2] if beam[2] in 'UD' else 'UD'

    return reflections[beam[2]][char]


energized = set()
seen = set()
while len(beams) > 0:
    beam = beams.pop()
    i, j = (beam[0] + directions[beam[2]][0], beam[1] + directions[beam[2]][1])

    # Beam got to the end of the grid or is a beam we already saw before
    if i >= R or j >= C or i < 0 or j < 0 or beam in seen:
        
        continue

    seen.add(beam)
    energized.add((i,j))
    if grid[i][j] == '.':
        beam = (i,j,beam[2])
        beams.append(beam)
        continue

    # If we got here, the beam will be deflected, so we can delete it

    for d in beam_deflect(beam, i, j, grid[i][j]):
        beam = (i,j,d)
        beams.append(beam)

print(len(energized))

for i,line in enumerate(grid):
    print("\n", end='')

    for j,c in enumerate(line):
        if (i,j) in energized:
            print('#', end='')
        else:
            print('.', end='')
    
print()
