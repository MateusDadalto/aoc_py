from collections import deque

path = "day_07.txt"
# path = "test.txt"

with open(path) as f:
    grid = [l.strip() for l in f.readlines()]

ROW_SIZE = len(grid)
COL_SIZE = len(grid[0])

source = (0, grid[0].find('S'))

split = 0

beams = set([(source[0]+1, source[1])])
print(beams)

queue = deque(beams)

def is_splitter(point, grid):
    row = point[0]
    col = point[1]
    
    return grid[row][col] == '^'

while len(queue) > 0:
    current = queue.popleft()
    # print(current)
    next_mov = (current[0]+1, current[1])
    row = next_mov[0]
    col = next_mov[1]
    
    if next_mov in beams or row >= ROW_SIZE or col >= COL_SIZE:
        continue
    
    if is_splitter(next_mov, grid):
        split += 1
        right_beam = (row, col+1)
        left_beam = (row, col-1)
        
        if right_beam not in beams:        
            queue.append(right_beam)
            beams.add(right_beam)
        
        if left_beam not in beams:
            queue.append(left_beam)
            beams.add(left_beam)
    else:
        queue.append(next_mov)
        beams.add(next_mov)

print(split)