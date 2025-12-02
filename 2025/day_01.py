path = "day_01.txt"
# path = "test.txt"

operation = {
    'L': -1,
    'R': 1
    }

part1 = 0
counter = 0
t = 50
with open(path) as f:
    lines = f.readlines()
    
    for l in lines:
        l = l.strip()
        o = l[0]
        n = int(l[1:])
        
        for _ in range(n):
            t += operation[o]
            
            t = t%100
            
            if t == 0:
                counter += 1
                
        if t == 0:
            part1 += 1

            
print("Day 1 part 1: ", part1)
print("Day 1 part 2: ", counter)