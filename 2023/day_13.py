
path = "day_13.txt"
# path = "test.txt"

with open(path, 'r') as file:
    blocks = [lines.split() for lines in file.read().split('\n\n')]

def compare_mirrored(line, i, j, distance):
    for k in range(0, distance):
        
        if line[i-k] != line[j + k]:
            return False

    return True                

def find_reflection(block:list[str]):
    for i in range(len(block) - 1):
        j = i+1
        if block[i] == block[j]:
            distance = min(j, len(block) - j)
            if compare_mirrored(block, i, j, distance):
                return (i, j, distance)
    
    return []

column_grids = [[list(row) for row in zip(*b)] for b in blocks]
# print(column_grids)
a = [find_reflection(b) for b in column_grids]
b = [find_reflection(b) for b in blocks]
# print(a, b)
answer =  sum([t[1] for t in a if len(t) > 0]) + sum([t[1]*100 for t in b if len(t) > 0])
print(answer)
