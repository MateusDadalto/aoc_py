path = "day_05.txt"
# path = "test.txt"

with open(path) as f:
    ranges, ids = f.read().split('\n\n')

range_lines = [tuple(map(int,l.strip().split('-'))) for l in ranges.split("\n")]

def is_in_range(n: int, ranges: tuple[int,int]):
    
    return any([ x <= n <= y for (x,y) in ranges])


counter = 0
for x in ids.split("\n"):
    x = int(x)
    
    if is_in_range(x, range_lines):
        counter += 1
        
        
print("Day 5 part 1:", counter)