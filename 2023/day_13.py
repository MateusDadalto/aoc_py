
path = "day_13.txt"
# path = "test.txt"

with open(path, 'r') as file:
    blocks = [lines.split() for lines in file.read().split('\n\n')]

def compare_mirrored(block, i, j, distance, smudged):
    for k in range(1, distance):
        differences = sum([1 for a,b in zip(block[i-k], block[j + k]) if a != b])
        if not smudged and differences == 1:
            smudged = True
        elif smudged and differences > 0:
            return False

    return smudged              

def find_reflection(block:list[str]):
    for i in range(len(block) - 1):
        j = i+1
        smudged = False
        differences = sum([1 for a,b in zip(block[i], block[j]) if a != b])
        smudged = differences >= 1
        if differences <= 1:
            distance = min(j, len(block) - j)
            if compare_mirrored(block, i, j, distance, smudged):
                return (i, j, distance)
    
    return []

column_grids = [[list(row) for row in zip(*b)] for b in blocks]
a = [find_reflection(b) for b in column_grids]
b = [find_reflection(b) for b in blocks]
answer =  sum([t[1] for t in a if len(t) > 0]) + sum([t[1]*100 for t in b if len(t) > 0])
print(answer)
