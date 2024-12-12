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


def count_continuous_lines(area):
    corners = {
        "NE": [(0, 1), (-1, 0), (-1,1)],
        "NW": [(0, -1), (-1, 0), (-1,-1)],
        "SE": [(0, 1), (1, 0), (1,1)],
        "SW": [(0, -1), (1, 0), (1,-1)],
    }
    counter = 0
    for a in area:
        for c in corners:
            c1 = corners[c][0]
            c2 = corners[c][1]
            c3 = corners[c][2]

            # external
            if (a[0]+c1[0], a[1]+c1[1]) not in area and  (a[0]+c2[0], a[1]+c2[1]) not in area:
                counter += 1
            
            # internal
            elif (a[0]+c1[0], a[1]+c1[1]) in area and  (a[0]+c2[0], a[1]+c2[1]) in area and (a[0]+c3[0], a[1]+c3[1]) not in area:
                counter +=1

    return counter


def find_area(grid, row, col):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    visited = set()
    label = grid[row][col]
    to_visit = deque([(row, col)])
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

    x_sides = set([i[0] for i in visited])
    y_sides = set([i[1] for i in visited])

    return visited, perimeter, count_continuous_lines(visited)


areas = []
visited = set()
total = 0
total_p2 = 0
for row in range(ROWS):
    for col in range(COLS):
        if (row, col) not in visited:
            area, perimeter, sides = find_area(lines, row, col)
            # print(area, perimeter, sides)
            total += len(area) * perimeter
            total_p2 += len(area) * sides
            visited.update(area)

print(total)
print(total_p2)
