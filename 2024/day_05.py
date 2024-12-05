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
    
p1 = 0

for i in instructions:
    numbers = [int(j) for j in i.split(',')]
    
    valid = True
    for n in range(len(numbers)):
        before = numbers[:n]
        after = numbers[n+1:]
        
        number = numbers[n]
        rule = rules.get(str(number), deepcopy(default))
        
        # The most confusing line ever written in software history
        if any([a not in rule.get("before") for a in after]) or any([b not in rule.get("after") for b in before]):
            valid = False
            
    if valid:
        p1 += numbers[int(len(numbers)/2)]
        
print(p1)