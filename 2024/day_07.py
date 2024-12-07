from itertools import cycle
from itertools import product
from functools import reduce

path = "day_07.txt"
# path = "test.txt"

with open(path) as f:
    lines = [l.strip() for l in f.readlines()]

p1 = 0

solved = set()
for line in lines:
    result, numbers = line.split(':')
    result = int(result)
    numbers = [int(i) for i in numbers.split()]
    
    n_op = len(numbers) - 1
    
    for operators in product('*+', repeat=n_op):
        op = iter(operators)
        calculation = reduce(lambda x, y: x+y if next(op) == '+' else x*y, numbers)

        if calculation == result:
            p1 += result
            solved.add(line)
            break


print("Part 1:", p1)
p2 = p1
def operation(x,y, op):
    if op == '+':
        return x+y
    
    if op == '*':
        return x*y
    
    return int(str(x)+str(y))

for line in lines:
    if line not in solved:
        result, numbers = line.split(':')
        result = int(result)
        numbers = [int(i) for i in numbers.split()]

        n_op = len(numbers) - 1

        for operators in product('*+|', repeat=n_op):
            op = iter(operators)
            calculation = reduce(lambda x, y: operation(x,y, next(op)), numbers)

            if calculation == result:
                p2 += result
                solved.add(line)
                break

print("Part 2:", p2)