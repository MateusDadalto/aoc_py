from collections import deque
from functools import cache


path = "day_21.txt"
# path = "test.txt"

directions = {(0, 1): ">", (1, 0): "v", (0, -1): "<", (-1, 0): "^"}
inverted_directions = {v: k for k, v in directions.items()}

numeric_kb = {
    (0, 0): '7', (0, 1): '8', (0, 2): '9',
    (1, 0): '4', (1, 1): '5', (1, 2): '6',
    (2, 0): '1', (2, 1): '2', (2, 2): '3',
    (3, 0): '#', (3, 1): '0', (3, 2): 'A'
}
inverted_numeric_kb = {v: k for k, v in numeric_kb.items()}

directional_kb = {
    (0, 0): '#', (0, 1): '^', (0, 2): 'A',
    (1, 0): '<', (1, 1): 'v', (1, 2): '>'
}
inverted_directional_kb = {v: k for k, v in directional_kb.items()}

def get_kb_maps(is_first):
    if is_first:
        return numeric_kb, inverted_numeric_kb
    
    return directional_kb, inverted_directional_kb

with open(path) as f:
    instructions = [l.strip() for l in f.readlines()]

def is_valid_path(start, steps, is_first):
    current = start
    keyboard, inverted_kb = get_kb_maps(is_first)
    pos = inverted_kb.get(start)
    for d in steps:
        move = inverted_directions[d]
        nxt_pos = (move[0] + pos[0], move[1] + pos[1])
        
        if nxt_pos not in keyboard or keyboard[nxt_pos] == '#':
            return False
        
        pos = nxt_pos 
    
    return True
        

@cache
def move_btn_and_press(start, target, is_first):
    _, inverted_kb = get_kb_maps(is_first)
    
    if start == target:
        return [['A']]

    pos_start = inverted_kb.get(start)
    pos_end = inverted_kb.get(target)
    
    diff_x = pos_end[0] - pos_start[0]
    diff_y = pos_end[1] - pos_start[1]

    direction_x = 0 if diff_x == 0 else diff_x // abs(diff_x)
    direction_y = 0 if diff_y == 0 else diff_y // abs(diff_y)
    
    if diff_x == 0 or diff_y == 0:
        return [[directions[(direction_x, direction_y)]] * abs(diff_x + diff_y) + ['A']]
    
    # if they are not aligned, the alternatives can be one or two (like 3->7 there are two ['<<^^', '^^<<'])
    option1 = [directions[(direction_x,0)]]*abs(diff_x) + [directions[(0, direction_y)]]*abs(diff_y)
    option2 = [directions[(0, direction_y)]]*abs(diff_y) + [directions[(direction_x,0)]]*abs(diff_x)
    
    return [i + ['A'] for i in (option1, option2) if is_valid_path(start, i, is_first)]

# Unit tests (visual assertions haha)
# print('A -> 9', move_btn('A','9', True))
# print('A -> 7', move_btn('A','7', True))
# print('3 -> 7', move_btn('3','7', True))
# print('7 -> 3', move_btn('7','3', True))
# print('A -> 4', move_btn('A','4', True))
# print('^ -> >', move_btn('^', '>', False))
# print('A -> <', move_btn('A', '<', False))
# print('< -> A', move_btn('<', 'A', False))
# print('< -> >', move_btn('<', '>', False))

@cache
def calculate_score(instruction, is_first):
    # don't care about scores on first, it is already going to give optimal results (I hope)
    if is_first:
        return 0
    
    _, inverted_kb = get_kb_maps(is_first)

    total = 0
    prev = 'A'
    for nxt in instruction:
        pos_prev = inverted_kb.get(prev)
        pos_nxt = inverted_kb.get(nxt)
        
        diff_x = pos_nxt[0] - pos_prev[0]
        diff_y = pos_nxt[1] - pos_prev[1]
        total += abs(diff_x) + abs(diff_y)
        prev = nxt
    
    return total
        
@cache
def process_instruction(instruction, is_first):
    
    if len(instruction) == 1:
        return [''.join(i) for i in move_btn_and_press('A', instruction[0], is_first)]
    
    moves = [''.join(i) for i in move_btn_and_press(instruction[-2], instruction[-1], is_first)]
    
    previous_possibilities = process_instruction(instruction[:-1], is_first)
    result = []
    
    for p in previous_possibilities:
        for move in moves:
            result.append(p+move)
    
    # min_score = min([calculate_score(i, is_first) for i in result])
    # print(min_score)
    # a = [i for i in result if min_score == calculate_score(i, is_first)]
    # print('start')
    # print(len(result))
    # print(len(a))
    # print('end')
    return result

# print(process_instruction('029A', True))

p1 = 0
for line in instructions:
    # print(f'start {line}')
    current = [line]
    for level in range(3):
        is_first = level==0
        temp = []
        for i in current:
            temp.extend(process_instruction(i, is_first))
        
        min_score = min([calculate_score(i, is_first) for i in temp])
        
        current = [i for i in temp if min_score == calculate_score(i, is_first)]
        
        print(level, end='\r')
    
    # print(level)
    # print(f'end {line}')

    # print(current)
    # print(len(min(current,key=len)))
    size = len(current[0])
    num = int(line[:3])
    print( f'{size} * {num}')
    p1 += size*num

print(p1)
    