
path = "day_13.txt"
# path = "test.txt"

with open(path, 'r') as file:
    blocks = [lines.split() for lines in file.read().split('\n\n')]

def compare_mirrored(line, i, j, distance):
    for k in range(0, distance):
        if line[i-k] != line[j + k]:
            return False

    return True                
            

def find_vertical_reflection(block: list[str]):
    possible = []
    first_line = block[0]
    for i in range(len(first_line) - 1):
        j = i+1
        if first_line[i] == first_line[j]:
            max_distance = min(j, len(first_line) - (j))
                
            if compare_mirrored(first_line, i, j, max_distance):
                possible.append((i, j, max_distance))

    for line in block[1:]:
        matches = [t for t in possible if compare_mirrored(line, *t)]
        if len(matches) == 0:
            return []

        possible = [t for t in matches if t in possible]

    # print(possible)
    return possible[0]

def find_horizontal_reflection(block:list[str]):
    for i in range(len(block) - 1):
        j = i+1
        if block[i] == block[j]:
            distance = min(j, len(block) - j)
            if compare_mirrored(block, i, j, distance):
                return (i, j, distance)
    
    return []


a = [find_vertical_reflection(b) for b in blocks]
b = [find_horizontal_reflection(b) for b in blocks]
print(a, b)
answer =  sum([t[1] for t in a if len(t) > 0]) + sum([t[1]*100 for t in b if len(t) > 0])
print(answer)
