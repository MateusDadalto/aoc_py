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

def is_valid_pt_2(n: int):
    primes = [2,3,5,7,11,13,17]
    n_str = str(n)
    n_size = len(n_str)
    
    for p in primes:
        if n_size%p == 0 and compare_sections(n_str, p):
            return False
    
    return True

def compare_sections(s: str, p: int):
    section_size = len(s)//p
    
    sections = set()
    for i in range(0, len(s), section_size):
        sections.add(s[i:i+section_size])
    
    # print(s, p, sections)
    return len(sections) == 1
    

part_1 = 0
part_2 = 0
for s in ranges:
    # print(s)
    start,end = s.split('-')
    
    valids = [i for i in range(int(start), int(end)+1) if not is_valid(i)]
    valids_2 = [i for i in range(int(start), int(end)+1) if not is_valid_pt_2(i)]
    # print(valids)
    part_1 += sum(valids)
    part_2 += sum(valids_2)


print("Day 2 part 1:", part_1)
print("Day 2 part 2:", part_2)
