import re
from itertools import permutations, product, combinations, combinations_with_replacement

path = "day_12.txt"
# path = "test.txt"

def validate_line(line, dist):
    matches = re.findall(r'#+', line)
    if len(matches) != len(dist):
        return False
    
    return not any(len(matches[i]) != dist[i] for i in range(len(matches)))

r = 0
options = { '?': ['.', '#'] }

with open(path, 'r') as file:
    for line in file:
        line = line.strip()
        springs, dist = line.split()
        springs = [c for c in springs]
        dist = [int(d) for d in dist.split(',')]
        questions = [i for i in range(len(springs)) if springs[i] == '?']
        # print(len(questions))

        for possibility in product(*[options.get(c, [c]) for c in springs]):
            # print(possibility)
            r += 1 if validate_line(''.join(possibility), dist) else 0

print(r)