from collections import defaultdict
from copy import deepcopy

path = "day_05.txt"
# path = "test.txt"

with open(path) as f:
    a,b = f.read().split("\n\n")
    orders = a.split()
    instructions = b.split()

default = {"before": [], "after":[]}

rules = {}

for order in orders:
    x,y = order.split('|')
    
    # numbers that X should come
    rule_x = rules.get(x, deepcopy(default))
    rule_y = rules.get(y, deepcopy(default))
    rule_x.get("before").append(int(y))
    rule_y.get("after").append(int(x))
    
    rules[x] = rule_x
    rules[y] = rule_y
    

def validate_rules(numbers, rules):
    for n in range(len(numbers)):
        before = numbers[:n]
        after = numbers[n+1:]
        
        number = numbers[n]
        rule = rules.get(str(number), default)
        
        # The most confusing line ever written in software history
        if any([a not in rule.get("before") for a in after]) or any([b not in rule.get("after") for b in before]):
            return False, n
    
    return True, 0
    
p1 = 0
invalid = []
for i in instructions:
    numbers = [int(j) for j in i.split(',')]
    
    valid, n = validate_rules(numbers, rules)
    
    if valid:
        p1 += numbers[int(len(numbers)/2)]
    else:
        invalid.append((numbers, n))
        
print(p1)

def swap(list, i, j): 
    tmp = list[i]
    list[i] = list[j]
    list[j] = tmp
    
    return list

def fix(numbers, n, rules):
    number = numbers[n]
    rule = rules.get(str(number), default)
    
    
    position = 0
    for i in range(len(numbers)):
        if i != n and numbers[i] in rule['after']:
            position += 1
    
    if position != n:
        return swap(numbers, position, n)
    
    return numbers

p2 = 0

while len(invalid) != 0:
    numbers, n = invalid.pop()
    
    fixed = fix(numbers, n, rules)
    
    valid, new_n = validate_rules(numbers, rules)
    
    if valid:
        p2 += numbers[int(len(numbers)/2)]
    else:
        invalid.append((fixed, new_n))

print(p2)