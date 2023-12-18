path = "day_18.txt"
# path = "test.txt"

map_d = ['R', 'D', 'L', 'U']

with open(path, 'r') as file:
    lines = [line.strip() for line in file]

def parse_line(l):
    d, n, color = l.split()
    d = map_d[int(color[-2:-1])]
    n = int('0'+color[2:-2], 16)
    n = int(n)

    return n if d in 'RD' else -n

x = 0
y = 0
area = 0
perimeter = 0
for horizontal, vertical in zip(lines[::2], lines[1::2]):
    x_n = parse_line(horizontal)
    y_n = parse_line(vertical)
    x += x_n
    y += y_n
    area += x*y_n
    perimeter += abs(x_n) + abs(y_n)
    
print(abs(area) + perimeter//2 + 1)