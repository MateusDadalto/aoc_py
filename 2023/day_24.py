from functools import cache
from itertools import permutations
from z3 import Real, Solver, Int, BitVec
path = "day_24.txt"
# path = "test.txt"

# equation terms for ax + b = y
@cache
def position(particle):
    x0,y0,z0,vx,vy,vz = particle

    return {'a': vy/vx, 'b':-(x0*vy)/vx + y0}


def intersect(p1, p2):
    p1_eq = position(p1)
    a = p1_eq['a']
    c = p1_eq['b']
    p2_eq = position(p2)
    b = p2_eq['a']
    d = p2_eq['b']

    if a == b:
        return None
    
    i = ((d-c)/(a-b), a*(d-c)/(a-b)+c)
    t1 = (i[0] - p1[0])/p1[3]
    t2 = (i[0] - p2[0])/p2[3]
    return i if t1 >= 0 and t2 >=0 else None
    

with open(path, 'r') as file:
    lines = [line.strip().split('@') for line in file]

particles = []
for p,v in lines:
    x0,y0,z0 = [int(x.strip()) for x in p.split(',')]
    vx,vy,vz = [int(x.strip()) for x in v.split(',')]
    particles.append((x0,y0,z0,vx,vy,vz))

pairs = set()

answer = 0
lower_limit = 200000000000000
higher_limit = 400000000000000
# lower_limit = 7
# higher_limit = 27
for p1,p2 in permutations(particles, 2):
    if (p1,p2) in pairs or (p2,p1) in pairs:
        continue
    pairs.add((p1,p2))

    i = intersect(p1, p2)

    if i and lower_limit <= i[0] <= higher_limit and lower_limit <= i[1] <= higher_limit:
        answer += 1

# part 2...
        
def solve(particles):
    I = lambda name: Real(name)
    x,y,z = I('x'), I('y'), I('z')
    vx,vy,vz = I('vx'), I('vy'), I('vz')

    solver = Solver()

    for i, p in enumerate(particles[:4]):
        x0,y0,z0,pvx,pvy,pvz = p
        t = I(f't{i}')
        solver.add(t>=0)
        solver.add(x + vx * t == x0 + pvx * t)
        solver.add(y + vy * t == y0 + pvy * t)
        solver.add(z + vz * t == z0 + pvz * t)
    
    print(solver.check())

    model = solver.model()
    rx, ry, rz = model.eval(x).as_long(), model.eval(y).as_long(), model.eval(z).as_long()
    return rx + ry + rz

print(solve(particles))