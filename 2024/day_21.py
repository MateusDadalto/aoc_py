from collections import deque


path = "day_21.txt"
# path = "test.txt"

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
    
    possible_paths = []
    mi = 1_000_000_000
    while len(q) > 0:
        current, steps = q.popleft()
        
        if len(steps) > mi:
            continue
        
        if current == target:
            mi = min(mi, len(steps))
            possible_paths.append([i for i in reversed(steps)])
            continue
    
        for d in directions:
            next_key = (current[0]+d[0], current[1]+d[1])
            
            if next_key in keyboard and keyboard[next_key] != '#':
                q.append((next_key, [directions[d]] + steps))
    
    return possible_paths

def build_sequence(instruction, keyboard):
    steps = [[]]
    # Start is A
    current = [key for key in keyboard if keyboard[key] == 'A'][0]
    for ch in instruction:
        # Don't look at this line
        target = [key for key in keyboard if keyboard[key] == ch][0]
        
        next_steps = move_btn(current, target, keyboard)
        possibilities = []
        for n in next_steps:
            possibilities.extend([s + n + ['A'] for s in steps])
            
        steps = possibilities
        current = target
    
    # [['<'], 'A', ['^'], 'A', ['>', '^', '^'], ['^', '>', '^'], ['^', '^', '>'], 'A', ['v', 'v', 'v'], 'A']
    
    return steps 

def run(possible_sequences, keyboard):
    
    m = 1_000_000_000
    results = []
    for sequence in possible_sequences:
        # every result of a single iteration will have the same len
        possible_results = build_sequence(sequence, keyboard)
        size = len(possible_results[0])
        if size == m:
            results.extend(possible_results)
        elif size < m:
            m = size
            results = possible_results
    
    return results    

p1 = 0
for instruction in instructions:
    
    numeric = int(instruction[:3])
    
    first_step = run([instruction], numeric_kb)
    # print(first_step)
    second_step = run(first_step, directional_kb)
    # print(''.join(second_step))
    third_step = run(second_step, directional_kb)
    size = len(third_step[0])
    # print(''.join(third_step))
    print( f'{size} * {numeric}')
    
    p1 += numeric*size
    
print(p1)
    