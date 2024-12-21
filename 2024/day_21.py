from collections import deque


path = "day_21.txt"
path = "test.txt"

directions = {(0, 1): ">", (1, 0): "v", (0, -1): "<", (-1, 0): "^"}

numeric_kb = {(0, 0): '7', (0, 1): '8', (0, 2): '9',
            (1, 0): '4', (1, 1): '5', (1, 2): '6',
            (2, 0): '1', (2, 1): '2', (2, 2): '3',
            (3, 0): '#', (3, 1): '0', (3, 2): 'A'}

directional_kb = {(0, 0): '#', (0, 1): '^', (0, 2): 'A',
                (1, 0): '<', (1, 1): 'v', (1, 2): '>'}


with open(path) as f:
    instructions = [l.strip() for l in f.readlines()]
    
def move_btn(start, target, keyboard):
    q = deque([(start, [])])
    
    while len(q) > 0:
        current, steps = q.popleft()
        
        if current == target:
            return [i for i in reversed(steps)]
    
        for d in directions:
            next_key = (current[0]+d[0], current[1]+d[1])
            
            if next_key in keyboard and keyboard[next_key] != '#':
                q.append((next_key, [directions[d]] + steps ))
    
    assert False, "Should never get here"

def build_sequence(instruction, keyboard):
    steps = []
    # Start is A
    current = [key for key in keyboard if keyboard[key] == 'A'][0]
    for ch in instruction:
        # Don't look at this line
        target = [key for key in keyboard if keyboard[key] == ch][0]
        
        steps = steps + move_btn(current, target, keyboard) + ['A']
        current = target
        
    return steps 
    
p1 = 0
for instruction in instructions:
    
    numeric = int(instruction[:3])
    
    first_step = build_sequence(instruction, numeric_kb)
    print(''.join(first_step))
    second_step = build_sequence(first_step, directional_kb)
    print(''.join(second_step))
    third_step = build_sequence(second_step, directional_kb)
    print(''.join(third_step))
    print( f'{len(third_step)} * {numeric}')
    
    p1 += numeric*len(third_step)
    
print(p1)
    