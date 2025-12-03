path = "day_02.txt"
# path = "test.txt"

with open(path) as f:
    ranges = [r.strip() for r in f.read().split(',')]
    
    
# print(ranges)

def is_valid(n: int):
    n_str = str(n)
    
    n_size = len(n_str)
    
    if n_size%2 != 0:
        return True
    
    if n_str[:n_size//2] == n_str[n_size//2:]:
        return False
    
    return True
    
count = 0
for s in ranges:
    print(s)
    start,end = s.split('-')
    
    valids = [i for i in range(int(start), int(end)+1) if not is_valid(i)]
    print(valids)
    count += sum(valids)


print(count)
    
