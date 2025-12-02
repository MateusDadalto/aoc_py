path = "day_01.txt"
# path = "test.txt"

operation = {
    'L': -1,
    'R': 1
    }

part1 = 0
counter = 0
current = 50
t = 50
with open(path) as f:
    lines = f.readlines()
    
    for l in lines:
        l = l.strip()
        o = l[0]
        n = int(l[1:])
        
        times_passed = n//100
        result = ((n%100) * operation[o]) + current
        
        if current != 0 and (result <= 0 or result >= 100):
            times_passed += 1

        current = result % 100
        
        counter += times_passed
        
        if current == 0:
            part1 += 1
            
print("Day 1 part 1: ", part1)
print("Day 1 part 2: ", counter) # 6671