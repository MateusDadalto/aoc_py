from math import prod

path = "day_06.txt"
# path = "test.txt"

with open(path) as f:
    
    lines = [l.split() for l in f.readlines()]
    

ROW_SIZE = len(lines)
COL_SIZE = len(lines[0])

part_1 = 0
for c in range(COL_SIZE):
    operation = lines[-1][c]
    total = 0 if operation == '+' else 1

    for r in range(ROW_SIZE - 1):
        value = int(lines[r][c])
        total = total + value if operation == '+' else total * value

    part_1 += total
    
print("Day 6 part 1:", part_1)

with open(path) as f:
    lines = [l[:-1] for l in f.readlines()]

ROW_SIZE = len(lines)
COL_SIZE = len(lines[0])

all = []
current = []
for c in reversed(range(COL_SIZE)):
    number_str = ''
    for r in range(ROW_SIZE - 1):
        char = lines[r][c]
        number_str = number_str + char
    
    if number_str.strip().isnumeric():
        current.append(int(number_str))
    elif number_str.isspace():
        all.append([c for c in current])
        current = []

all.append(current)

part_2 = 0
for numbers, operation in zip(all, reversed(lines[-1].split())):
    part_2 += sum(numbers) if operation == '+' else prod(numbers)


print("Day 6 part 2:", part_2)