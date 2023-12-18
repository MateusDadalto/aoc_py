path = "day_18.txt"
# path = "test.txt"

perimeter = [(0, 0)]

directions = {
    'L': (0, -1),
    'D': (1, 0),
    'R': (0, 1),
    'U': (-1, 0)
}

min_col = 2**32
max_col = 0
min_row = 2**32
max_row = 0
with open(path, 'r') as file:
    for line in file:
        line = line.strip()

        d, n, color = line.split()
        color = color[1:-1]

        for _ in range(int(n)):
            i, j = perimeter[-1]
            x, y = directions[d]
            new_i = i+x
            new_j = j+y

            min_col = min(new_j, min_col) 
            max_col = max(new_j, max_col) 
            min_row = min(new_i, min_row)
            max_row = max(new_i, max_row)

            perimeter.append((i+x, j+y))

assert perimeter[0] == perimeter[-1]
min_col -= 2
max_col += 2
min_row -= 2
max_row += 2
p = set(perimeter)
area = 0
# flood fill outiside
total_area = ((max_row + 1) - (min_row)) * ((max_col + 1)-(min_col))

empty = [(min_row, min_col)]
counted = set()
while len(empty) > 0:
    i,j = empty.pop()

    if (i,j) in counted:
        continue

    counted.add((i,j))
    for x, y in directions.values():
        new_i = x+i
        new_j = y+j
        # I'll go crazy, I've spend HALF AN HOUR with a bug in my number bc this SHIT had a typo in line 64
        # min_row <= new_j <= max_col instead of min_col <= new_j <= max_col
        if (new_i, new_j) not in p and \
            min_row <= new_i <= max_row and \
            min_col <= new_j <= max_col:

            empty.append((new_i, new_j))
    
# for i in range(min_row, max_row + 1):
#     print("\n", end='')

#     for j in range(min_col, max_col + 1):
#         if (i,j) in counted:
#             print('.', end='')
#         else:
#             print('#', end='')

print(total_area - len(counted))