from collections import deque

path = "day_10.txt"
# path = "test.txt"

directions = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

with open(path) as f:
    lines = [l.strip() for l in f.readlines()]
    

ROWS = len(lines)
COLS = len(lines[0])

trail_heads = []
for row in range(ROWS):
    for col in range(COLS):
        tile = lines[row][col]
        if tile.isnumeric() and int(tile) == 0:
            trail_heads.append((row,col))

def is_inside(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

total = 0

def count_score(grid, trail_head, part_2):
    score = 0
    visited_ends = set()
    tiles = [trail_head]
    
    while len(tiles) > 0:
        row, col = tiles.pop()
        height = int(grid[row][col])
        
        if (part_2 or (row, col) not in visited_ends) and height == 9:
            score += 1
            visited_ends.add((row, col))
            continue
        
        for r, c in directions:
            new_row = row + r
            new_col = col + c
            if is_inside(grid, new_row, new_col) and int(grid[new_row][new_col]) - height == 1:
                tiles.append((new_row, new_col))
            
    return score

print("p1:", sum([count_score(lines, i, False) for i in trail_heads]))
print("p2:", sum([count_score(lines, i, True) for i in trail_heads]))
