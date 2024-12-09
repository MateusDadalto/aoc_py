path = "day_08.txt"
# path = "test.txt"

with open(path) as f:
    lines = [l.strip() for l in f.readlines()]

ROWS = len(lines)
COLS = len(lines[0])

interst_points = []
letters = []
for row in range(ROWS):
    for col in range(COLS):
        if lines[row][col] != '.':
            interst_points.append((row,col))
            letters.append(lines[row][col])
            
def create_antinodes(p1, p2):
    distance = (p1[0] - p2[0], p1[1] - p2[1])
    
    a1 = (p1[0] + distance[0], p1[1] + distance[1])
    a2 = (p2[0] - distance[0], p2[1] - distance[1])
    
    return a1, a2

def create_antinodes_2(p1,p2, rows, cols):
    direction = (p1[0] - p2[0], p1[1] - p2[1])
    
    below_p1 = []
    above_p2 = []
    
    i = 1
    ax = p2[0]
    ay = p2[1]
    while 0 <= ax < rows and 0 <= ay < cols:
        below_p1.append((ax, ay))
        ax = p2[0] - (direction[0]*i)
        ay = p2[1] - (direction[1]*i)
        
        i += 1
    
    j = 1
    bx = p1[0]
    by = p1[1]
    while 0 <= bx < rows and 0 <= by < cols:
        above_p2.append((bx, by))
        bx = p1[0] + (direction[0]*j)
        by = p1[1] + (direction[1]*j)
        
        j += 1
    
    return below_p1 + above_p2
    
seen = []
antinodes = set()
antinodes_2 = set()
for k in interst_points:
    for j in interst_points:
        if k != j and lines[k[0]][k[1]] == lines[j[0]][j[1]] and set((k,j)) not in seen:
            a1,a2 = create_antinodes(k,j)
            a_p2 = create_antinodes_2(k, j, ROWS, COLS)
            seen.append(set((k,j)))
            antinodes_2.update(a_p2)
            # SPENT HALF AN HOUR DEBUGGING THIS FUCKER BECAUSE IT WAS <= COLS
            if 0 <= a1[0] < ROWS and 0<= a1[1] < COLS:
                antinodes.add(a1)
            if 0 <= a2[0] < ROWS and 0<= a2[1] < COLS:
                antinodes.add(a2)
                

print("p1:", len(antinodes))
print("p2:", len(antinodes_2))
