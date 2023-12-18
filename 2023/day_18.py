path = "day_18.txt"
# path = "test.txt"

map_d = ['R', 'D', 'L', 'U']
directions = {
    'L': (0, -1),
    'D': (1, 0),
    'R': (0, 1),
    'U': (-1, 0)
}

with open(path, 'r') as file:
    lines = [line.strip() for line in file]

def parse_line(l):
    d, n, color = l.split()
    d = map_d[int(color[-2:-1])]
    n = int('0'+color[2:-2], 16)
    n = int(n)

    return n, d

vertices = [(0,0)]
perimeter = 0
for l in lines:
    n, d = parse_line(l)
    x = vertices[-1]
    i,j = directions[d]

    perimeter += n
    vertices.append((x[0] + (i*n), x[1]+ (j*n)))

s = 0
for x1, x2 in zip(vertices, vertices[1:]):
    s += (x1[1] + x2[1]) * (x1[0] - x2[0])


print(abs(s/2) + perimeter/2 + 1)
    
    
    

    