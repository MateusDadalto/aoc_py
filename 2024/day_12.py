from itertools import cycle
from collections import deque

path = "day_12.txt"
# path = "test.txt"

with open(path) as f:
    lines = [l.strip() for l in f.readlines()]

# print(lines)
ROWS = len(lines)
COLS = len(lines[0])

def is_inside(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def find_area(grid, row, col):
    directions = [
        (0, -1),
        (1, 0),
        (0, 1),
        (-1, 0)
    ]
    visited = set()
    label = grid[row][col]
    to_visit = deque([(row,col)])
    perimeter = 0

    while len(to_visit) != 0:
        current = to_visit.popleft()
        if current in visited:
            continue

        visited.add(current)
        for d in directions:
            new_row = current[0] + d[0]
            new_col = current[1] + d[1]

            if (new_row, new_col) in visited:
                continue

            if is_inside(grid, new_row, new_col) and grid[new_row][new_col] == label:
                to_visit.append((new_row, new_col))
            else:
                perimeter += 1
    
    return visited, perimeter
            




areas = []
visited = set()
total = 0
for row in range(ROWS):
    for col in range(COLS):
        if (row,col) not in visited:
            area, perimeter = find_area(lines, row, col)
            # print(area, perimeter)
            total += len(area) * perimeter
            visited.update(area)

print(total)
