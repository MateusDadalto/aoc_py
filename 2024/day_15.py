from collections import Counter
from itertools import cycle
from typing import Set

path = "day_15.txt"
# path = "test.txt"

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
        if not success:
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


for char in commands:
    robot, boxes = move(robot, char, walls, boxes)
    # print_grid(ROWS, COLS, robot, walls, boxes, char)

p1 = sum([100*i[0] + i[1] for i in boxes])

print(p1)

print_grid(ROWS, COLS, robot, walls, boxes, char)
