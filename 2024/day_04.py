from collections import Counter
path = "day_04.txt"
# path = "test.txt"

with open(path) as f:
    lines = [l.strip() for l in f.readlines()]

ROW_SIZE = len(lines)
COL_SIZE = len(lines[0])

def is_mas(lines, i, j, x, y):

    for k, c in [(1, "M"), (2, "A"), (3, "S")]:
        row = x * k + i
        col = y * k + j

        if not (0 <= row < ROW_SIZE and 0 <= col < COL_SIZE and lines[row][col] == c):
            return False

    return True


def count_xmas(lines, i, j, counter):
    neighbours = [(1, 0), (1, -1), (0, -1), (-1,-1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

    for x, y in neighbours:
        counter += 1 if is_mas(lines, i, j, x, y) else 0

    return counter


total = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):

        if lines[i][j] == "X":
            total += count_xmas(lines, i, j, 0)

print(total)

### part 2

def check_diagonal_mas(lines, i, j):
    diag = [(0,0), (1,1), (2,2)]
    
    return all([ch in [lines[i+x][j+y] for x,y in diag] for ch in ['M', 'A', 'S']])

def x_mas(lines, i, j):
    corners = [(0,0), (2,0), (0,2), (2,2)]
    center =  (1,1)
    
    corner_letters = Counter([lines[i+x][j+y] for x,y in corners])
    if corner_letters.get('M', 0) == 2 and corner_letters.get('S', 0) == 2:
        return check_diagonal_mas(lines, i, j)
    
    return False
    
p2 = 0
for i in range(ROW_SIZE - 2):
    for j in range(COL_SIZE - 2):
        center = lines[i+1][j+1]
        
        if center == "A" and x_mas(lines, i, j):
            p2 += 1
            
print(p2)