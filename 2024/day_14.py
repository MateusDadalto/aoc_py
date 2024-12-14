import re
from collections import Counter

path = "day_14.txt"
# path = "test.txt"

def parse_robots(m):
    return tuple([int(i) for i in re.findall(r'-?\d+', m)])

    
with open(path) as f:
    robots = [parse_robots(i) for i in f.readlines()]
    
    
seconds = 100

ROWS = 103
COLS = 101
HALF_R = ROWS//2
HALF_C = COLS//2
final_positions = []

quadrants = {1:0, 2:0, 3:0, 4:0}

def calculate_position(robot, seconds):
    x0,y0,vx,vy = robot
    
    x = x0 + vx*seconds
    y = y0 + vy*seconds
    
    row = y%ROWS
    col = x%COLS
    
    return (row, col)

for robot in robots:
    row, col = calculate_position(robot, 100)
    final_positions.append((row,col))
    
    if row < HALF_R and col < HALF_C:
        quadrants[1] += 1
    
    if row < HALF_R and col > HALF_C:
        quadrants[2] += 1
        
    if row > HALF_R and col < HALF_C:
        quadrants[3] +=1
    
    if row > HALF_R and col > HALF_C:
        quadrants[4] +=1
    
p1 = 1
print (quadrants)
for i in quadrants:
    p1 *= quadrants[i]

print(p1)

def print_robots(rows, cols, positions, seconds):
    print(f'Seconds: {seconds}')
    p = Counter(positions)
    for r in range(rows):
        print()
        for c in range(cols):
            if (r,c) in p:
                print(p.get((r,c)), end='')
            else:
                print('.', end='')
                
    print()
    print('='*cols)
    print()

i = 0
while True:
    i += 1
    positions = []
    middle = 0
    delta_r = HALF_R//3
    delta_c = HALF_C//3
    middle_area = (2*delta_r) * (2*delta_c)
    
    for robot in robots:
        row, col = calculate_position(robot,i)
        positions.append((row,col))
        
        if HALF_C - delta_c < col < HALF_C + delta_c and HALF_R - delta_r < row < HALF_R + delta_r:
            middle += 1
    
    
    
    concentration = middle/middle_area * 100
    if concentration > 15:
        found = True
        print(f'Middle concentration: {concentration:.2f}')
        
        print_robots(ROWS, COLS, positions, i)
        break
        
            