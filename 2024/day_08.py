from collections import defaultdict, Counter

path = "day_08.txt"
# path = "test.txt"

with open(path) as f:
    lines = [l.strip() for l in f.readlines()]

ROWS = len(lines)
COLS = len(lines[0])

interst_points = []
letters = []
for row in range(ROWS):
    for col in range(COLS):
        if lines[row][col] != '.':
            interst_points.append((row,col))
            letters.append(lines[row][col])
            
def create_antinodes(p1, p2):
    distance = (p1[0] - p2[0], p1[1] - p2[1])
    
    a1 = (p1[0] + distance[0], p1[1] + distance[1])
    a2 = (p2[0] - distance[0], p2[1] - distance[1])
    
    return a1, a2
    
seen = []
antinodes = set()
pairs = 0
out = 0
_in = 0
for k in interst_points:
    for j in interst_points:
        if k != j and lines[k[0]][k[1]] == lines[j[0]][j[1]] and set((k,j)) not in seen:
            pairs += 1
            a1,a2 = create_antinodes(k,j)
            
            seen.append(set((k,j)))
            # SPENT HALF AN HOUR DEBUGGING THIS FUCKER BECAUSE IT WAS <= COLS
            if 0 <= a1[0] < ROWS and 0<= a1[1] < COLS:
                antinodes.add(a1)
                _in += 1
            else:
                out += 1
            if 0 <= a2[0] < ROWS and 0<= a2[1] < COLS:
                antinodes.add(a2)
                _in += 1
            else:
                out += 1
                

print(len(antinodes))
# print("out", out)
# print("in", _in)
# print("pairs", pairs)
# c = Counter(letters)
# expected_p = 0
# for i in c:
#     expected_p += sum(range(c[i]))

# print("expected", expected_p)

# for row in range(ROWS):
#     for col in range(COLS):
#         if (row, col) in antinodes:
#             print('#', end='')
#         else:
#             print(lines[row][col], end='')
#     print()
            