path = "day_10.txt"
# path = "test.txt"

sequences = []
with open(path, 'r') as file:
    grid = [[c for c in line.strip()] for line in file]
    
def connections(c, row, col):
    if c == '|':
        return [(row -1, col), (row + 1, col)]
    elif c == '-':
        return [(row, col - 1), (row, col + 1)]
    elif c == 'L':
        return [(row - 1, col), (row, col + 1)]
    elif c == 'J':
        return [(row - 1, col), (row, col - 1)]
    elif c == '7':
        return [(row + 1, col), (row, col - 1)]
    elif c == 'F':
        return [(row + 1, col), (row, col + 1)]
    
    return []

def define_pipe(con):
    assert len(con) == 2
    
    c1, c2 = con

    borders = (c1[1] - c2[1], c1[2] - c2[2])

    if borders == (-1, 1):
        return 'F'
    elif borders == (1, 1):
        return 'L'
    elif borders == (1, -1):
        return 'J'
    elif borders == (-1, 1):
        return '7'
    elif borders[0] == 0:
        return '-'
    elif borders[1] == 0:
        return '|'
    
    assert False, f"All cases should be covered. Connections:{con}, borders: {borders}" 

    

max_col = len(grid[0])
max_row = len(grid)
start = (0,0)
start_pipe = '.'

for i in range(max_row):
    for j in range(max_col):
        if grid[i][j] == 'S':
            start = (i, j)
            connected = []
            for ii,jj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                n_i = i + ii
                n_j = j + jj
                if (i,j) in connections(grid[n_i][n_j], n_i, n_j):
                    connected.append((grid[n_i][n_j], n_i, n_j))
            
            start_pipe = define_pipe(connected)
            grid[i][j] = start_pipe
            
looped = False
row, col = start
loop = []
previous = start
nxt = None
while (not looped):
    loop.append((grid[row][col], row, col))
    c = connections(grid[row][col], row, col)

    assert len(c) == 2, f"current should be a pipe. Current: {grid[col][row]}, row: {row}, col: {col}"
    new_row, new_col = c[0] if c[0] != previous else c[1]
    
    previous = (row, col)
    row = new_row
    col = new_col

    looped = row == loop[0][1] and col == loop[0][2]
    
print(len(loop) // 2)