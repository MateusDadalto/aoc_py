path = "day_04.txt"
# path = "test.txt"

with open(path) as f:
    lines = [l.strip() for l in f.readlines()]

ROW_SIZE = len(lines)
COL_SIZE = len(lines[0])
        
def is_paper(point: tuple[int, int], grid: list[list[str]]):
    r,c = point
    
    return 0 <= r < ROW_SIZE and 0 <= c < COL_SIZE and grid[r][c] == '@'

def is_accessible(point: tuple[int, int], grid: list[list[str]]):
    neighbours = [(1, 0), (1, -1), (0, -1), (-1,-1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
    
    roll_count = 0
    for (i,j) in neighbours:
        coord = (point[0] + i, point[1] + j)
        
        if is_paper(coord, grid):
            roll_count += 1
        
        if roll_count >= 4:
            return False
    
    return True

counter = 0
for i in range(ROW_SIZE):
    for j in range(COL_SIZE):
        if lines[i][j] == '@' and is_accessible((i,j), lines):
            # print(i,j)
            counter += 1
            
print(counter)