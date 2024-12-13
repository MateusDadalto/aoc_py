from collections import deque
import re
import numpy as np

path = "day_13.txt"
path = "test.txt"

def parse_machine(m):
    a,b,prize = [re.findall(r'\d+', item) for item in m]

    return (int(a[0]), int(a[1])), (int(b[0]), int(b[1])), (int(prize[0]), int(prize[1]))

def is_divisble(i,j):
    return i%j == 0

with open(path) as f:
    machines = [parse_machine(i.splitlines()) for i in f.read().split('\n\n')]

tokens = 0
for m in machines:
    a1, a2 = m[0]
    b1, b2 = m[1]
    c1,c2 = m[2]


    
    B = (c2*a1-a2*c1)/(b2*a1-a2*b1)
    A = (c1-b1*B)/a1
    print("B", (c2*a1-a2*c1)/(b2*a1-a2*b1))
    print("A", (c1-b1*B)/a1)

    if 0<=A<=100 and 0<=B<=100 and A.is_integer() and B.is_integer():
        assert a1*A + b1*B == c1, f"Equation 1 do not check: {a1}*{A} + {b1}*{B} = {c1}"
        assert a2*A + b2*B == c2, f"Equation 2 do not check: {a2}*{A} + {b2}*{B} = {c2}"

        tokens += 3*A + B

print(tokens)