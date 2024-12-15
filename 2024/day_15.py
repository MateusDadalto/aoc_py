from collections import Counter
from itertools import cycle
from typing import Set
from copy import deepcopy

path = "day_15.txt"
path = "test.txt"

directions = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}


def print_grid(rows, cols, robot, walls, boxes, char):
    print("move: ", char)
    for r in range(rows):
        print()
        for c in range(cols):
            if (r, c) == robot:
                print("@", end="")
            elif (r, c) in walls:
                print("#", end="")
            elif (r, c) in boxes:
                print("O", end="")
            else:
                print(".", end="")

    print()
    print('='*cols)
    print()


with open(path) as f:
    input1, input2 = f.read().split("\n\n")

    grid = input1.splitlines()
    commands = ''.join([i.strip() for i in input2.splitlines()])

ROWS = len(grid)
COLS = len(grid[0])

# print_grid(ROWS, COLS, grid)

walls = set()
boxes = set()

for row in range(ROWS):
    for col in range(COLS):

        if grid[row][col] == "@":
            robot = (row, col)
        elif grid[row][col] == "#":
            walls.add((row, col))
        elif grid[row][col] == "O":
            boxes.add((row, col))


# print_grid(ROWS, COLS, robot, walls, boxes)


def move_box(box, direction, walls, boxes: Set):
    d = directions[direction]
    next_tile = (box[0] + d[0], box[1] + d[1])

    if next_tile in walls:
        return False, boxes

    if next_tile in boxes:
        success, new_boxes = move_box(next_tile, direction, walls, boxes)
        # if success:
        #     return move_box(box, direction, walls, new_boxes)
        if success:
            return move_box(box, direction, walls, new_boxes)
        else:
            return False, boxes

    new_boxes = boxes
    new_boxes.remove(box)
    new_boxes.add(next_tile)

    return True, new_boxes


def move(obj, direction, walls, boxes):
    d = directions[direction]
    next_tile = (obj[0] + d[0], obj[1] + d[1])

    if next_tile in walls:
        return obj, boxes

    if next_tile in boxes:
        success, new_boxes = move_box(next_tile, direction, walls, boxes)
        if success:
            return next_tile, new_boxes
        else:
            return obj, boxes

    return next_tile, boxes

boxes_1 = deepcopy(boxes)
robot_1 = robot
for char in commands:
    robot_1, boxes_1 = move(robot_1, char, walls, boxes_1)
    # print_grid(ROWS, COLS, robot, walls, boxes, char)

p1 = sum([100*i[0] + i[1] for i in boxes_1])

print(p1)

print_grid(ROWS, COLS, robot_1, walls, boxes_1, char)

def convert_p2(obj, is_robot):
    r,c = obj
    
    new_c = 2*c
    
    if is_robot:
        return (r, new_c), None
    
    return (r, new_c), (r, new_c+1)

walls_2 = set()
## https://stackoverflow.com/questions/3204245/how-do-i-convert-a-tuple-of-tuples-to-a-one-dimensional-list-using-list-comprehe
walls_2.update(sum((convert_p2(i, False) for i in walls), ()))
boxes_2 =set([convert_p2(i, False) for i in boxes])
print(boxes_2)
robot_2, _ = convert_p2(robot, True)
ROWS_2 = ROWS
COLS_2 = COLS * 2

def print_grid2(rows, cols, robot, walls, boxes, char):
    b = cycle('[]')
    plain_boxes = set()
    plain_boxes.update([tile for box in boxes for tile in box])
    print("move: ", char)
    for r in range(rows):
        print()
        for c in range(cols):
            if (r, c) == robot:
                print("@", end="")
            elif (r, c) in walls:
                print("#", end="")
            elif (r, c) in plain_boxes:
                print(next(b), end="")
            else:
                print(".", end="")

    print()
    print('='*cols)
    print()

# print_grid2(ROWS_2, COLS_2, robot_2, walls_2, boxes_2, '')

def possible_vertical(next_tiles):
    
    left = next_tiles[0]
    right = next_tiles[1]
    
    return ((left[0], left[1] - 1), left), (left, right), (right, (right[0], right[1]+1))
    

def move_box_2(box, direction, walls, boxes: Set):
    d = directions[direction]
    
    next_tile_left = (box[0][0] + d[0], box[0][1] + d[1])
    next_tile_right = (box[1][0] + d[0], box[1][1] + d[1])
    
    next_box = (next_tile_left, next_tile_right)
    new_boxes = deepcopy(boxes)
    
    if next_tile_left in walls or next_tile_right in walls:
        return False, boxes
    
    if direction == '>' and (next_tile_right, (next_tile_right[0] + d[0], next_tile_right[1] + d[1])) in boxes:
        success, new_boxes = move_box_2((next_tile_right, (next_tile_right[0] + d[0], next_tile_right[1] + d[1])), direction, walls, boxes)
        
    if direction == '<' and ((next_tile_left[0] + d[0], next_tile_left[1] + d[1]), next_tile_left) in boxes:
        success, new_boxes = move_box_2(((next_tile_left[0] + d[0], next_tile_left[1] + d[1]), next_tile_left), direction, walls, boxes)
        
    if direction in '^v' and any([i in boxes for i in possible_vertical(next_box)]):
        next_boxes = [i for i in possible_vertical(next_box) if i in boxes]
        
        new_boxes = deepcopy(boxes)
        for b in next_boxes:
            success, new_boxes = move_box_2(b, direction, walls, new_boxes)
            if not success:
                return False, boxes
        
    new_boxes.remove(box)
    new_boxes.add(next_box)

    return True, new_boxes

def move_2(robot, direction, walls, boxes):
    d = directions[direction]
    next_tile = (robot[0] + d[0], robot[1] + d[1])

    new_boxes = deepcopy(boxes)
    robot_possible_vertical = [((next_tile[0], next_tile[1] - 1), next_tile), (next_tile, (next_tile[0], next_tile[1] + 1))]

    if next_tile in walls:
        return robot, boxes
    
    if direction in '>' and (next_tile, (next_tile[0] + d[0], next_tile[1] + d[1])) in boxes:
        success, new_boxes = move_box_2((next_tile, (next_tile[0] + d[0], next_tile[1] + d[1])), direction, walls, boxes)
        
        if not success:
            return robot, boxes
    elif direction in '<' and ((next_tile[0] + d[0], next_tile[1] + d[1]), next_tile) in boxes:
        success, new_boxes = move_box_2(((next_tile[0] + d[0], next_tile[1] + d[1]), next_tile), direction, walls, boxes)
        
        if not success:
            return robot, boxes
    elif direction in '^v' and any(i in boxes for i in robot_possible_vertical):
        next_box = [i for i in robot_possible_vertical if i in boxes][0]
        
        new_boxes = deepcopy(boxes)
        success, new_boxes = move_box_2(next_box, direction, walls, new_boxes)
        if not success:
            return robot, boxes
    
    return next_tile, new_boxes

print_grid2(ROWS_2, COLS_2, robot_2, walls_2, boxes_2, 'no move')


for char in commands:
    robot_2, boxes_2 = move_2(robot_2, char, walls_2, boxes_2)
    print_grid2(ROWS_2, COLS_2, robot_2, walls_2, boxes_2, char)
    input()

# p1 = sum([100*i[0] + i[1] for i in boxes_1])

# print(p1)

print_grid2(ROWS_2, COLS_2, robot_2, walls_2, boxes_2, '')
# print_grid(ROWS, COLS, robot_1, walls, boxes_1, char)