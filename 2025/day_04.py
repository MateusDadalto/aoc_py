path = "day_04.txt"
# path = "test.txt"

with open(path) as f:
    lines = [l.strip() for l in f.readlines()]

ROW_SIZE = len(lines)
COL_SIZE = len(lines[0])
        
def is_paper(point: tuple[int, int], grid: list[list[str]], removed: set[tuple[int,int]]):
    r,c = point
    
    return point not in removed and 0 <= r < ROW_SIZE and 0 <= c < COL_SIZE and grid[r][c] == '@'

def is_accessible(point: tuple[int, int], grid: list[list[str]], removed: set[tuple[int,int]]):
    neighbours = [(1, 0), (1, -1), (0, -1), (-1,-1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
    
    roll_count = 0
    for (i,j) in neighbours:
        coord = (point[0] + i, point[1] + j)
        
        if is_paper(coord, grid, removed):
            roll_count += 1
        
        if roll_count >= 4:
            return False
    
    
    return True

def find_accessibles(grid: list[list[str]], removed: set[tuple[int,int]]):
    counter = 0
    for i in range(ROW_SIZE):
        for j in range(COL_SIZE):
            if (i,j) not in removed and lines[i][j] == '@' and is_accessible((i,j), grid, removed):
                # print(i,j)
                removed.add((i,j))
                counter += 1
            
    return counter, removed

print("Day 4 part 1:", find_accessibles(lines, set())[0])

removed = set()

stop = False
limit = 0
while not stop:
    found, removed = find_accessibles(lines, removed)
    limit += 1
    if found == 0:
        stop = True

print("Day 4 part 2:", len(removed))