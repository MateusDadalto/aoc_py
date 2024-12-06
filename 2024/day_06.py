from itertools import cycle

path = "day_06.txt"
# path = "test.txt"

with open(path) as f:
    lines = [l.strip() for l in f.readlines()]

ROWS = len(lines)
COLS = len(lines[0])

directions = {">": (0,1), 'v': (1,0), '<': (0,-1), '^': (-1, 0)}

loop = cycle(directions)

initial_pos = ()
d = ()
for i in range(ROWS):
    print(lines[i])
    for j in range(COLS):
        if lines[i][j] in directions:
            initial_pos = (i,j)
            d = directions[lines[i][j]]
            
            while next(loop) != lines[i][j]:
                print("next")
            

print(initial_pos)
print(d)

def is_inside(lines, pos):
    return 0 <= pos[0] < ROWS and 0<= pos[1] < COLS

def walk(lines, pos, d):
    i,j = pos
    x,y = d
    
    new_pos = (x+i, y+j)
    if is_inside(lines, new_pos) and lines[new_pos[0]][new_pos[1]] == '#':
        return pos, directions[next(loop)]
        
    return new_pos, d

inside = True
pos = initial_pos
print("direction",d)
print("initial pos", pos)
walked = set()
while inside:
    walked.add(pos)
    pos, d = walk(lines, pos, d)
    print("next pos", pos)
    print("next d", d)
    
    inside = is_inside(lines, pos)

print(walked)
print(len(walked))