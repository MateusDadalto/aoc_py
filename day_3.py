path = "day_3.txt"
# path = "test.txt"

with open(path, 'r') as file:
    lines = [line.strip() for line in file]
    size = len(lines[0])
    lines = ''.join(lines)


symbols = []

accumulator = ''
acc_indexes = []
digits = {}
for i, c in enumerate(lines):
    if c.isdigit():
        accumulator += c
        acc_indexes.append(i)
        continue
    elif accumulator != '':
        for j in acc_indexes:
            digits[j] = (int(accumulator), acc_indexes)
        
        accumulator = ''
        acc_indexes = []
        
    if c == '.':
        continue


    symbols.append((i))

gears = []
neighboors = [-size -1, -size, -size +1, +1, size + 1, size, size -1, -1]
for symbol in symbols:
    total_n = []
    visited = []
    for n in neighboors:
        i = symbol + n
        if i in visited:
            continue

        value, indexes = digits.pop(i, (0, []))
        if value != 0:
            total_n.append(value)
            visited.extend(indexes)
    
    if len(total_n) == 2:
        gears.append(total_n[0]*total_n[1])
            

print(sum(gears))
