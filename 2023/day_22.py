from collections import defaultdict

path = "day_22.txt"
# path = "test.txt"

# Melting my head with conditions
def collision(brick0, brick1):
    x0_0, y0_0, z0_0, x0_1, y0_1, z0_1 = brick0
    x1_0, y1_0, z1_0, x1_1, y1_1, z1_1 = brick1

    # don't collide if b0 ends before b1 starts or b0 starts after b1 ends
    x_collide = not (x0_1 < x1_0 or x0_0 > x1_1)
    y_collide = not (y0_1 < y1_0 or y0_0 > y1_1)
    z_collide = not (z0_1 < z1_0 or z0_0 > z1_1)
    return x_collide and y_collide and z_collide

def is_supported(brick0, brick1):
    x0, y0, z0, x1, y1, z1 = brick0
    return collision((x0, y0, z0-1, x1, y1, z1-1), brick1)

def fall(brick, bricks, removed):
    x0, y0, z0, x1, y1, z1 = brick
    removed = removed or []
    if z0 == 1:
        return brick

    while z0 > 1:
        if any(collision((x0, y0, z0-1, x1, y1, z1-1), b1) for b1 in bricks[z0-1] if b1 not in removed):
            return (x0, y0, z0, x1, y1, z1)

        z0 -= 1
        z1 -= 1

    return (x0, y0, z0, x1, y1, z1)


with open(path, 'r') as file:
    positions = [l.strip().split('~') for l in file]

bricks = defaultdict(list)
total = len(positions)

for p in positions:
    x0, y0, z0, x1, y1, z1 = [int(i) for s in p for i in s.split(',')]
    bricks[z1].append((x0, y0, z0, x1, y1, z1))

# print(sorted(bricks), len(sorted(bricks)))

# The fall part is actually ok, I'm fine with this
f_bricks = defaultdict(list)
for z in sorted(bricks):
    for i,brick in enumerate(bricks[z]):
        fallen = fall(brick, f_bricks, None)
        f_bricks[fallen[-1]].append(fallen)

# This is insanity, 
# I'm using this bc my fallen dict saves the blocks based on their top z
# I need this one to iterate from below and know which blocks can be removed
f_bricks_start = defaultdict(list)
for k in f_bricks:
    for b in f_bricks[k]:
        f_bricks_start[b[2]].append(b)

# lets see which block cause another to fall when removed
chain_count = 0
sorted_z = [z for z in sorted(f_bricks) if len(f_bricks[z]) > 0]
for z in sorted_z:
    for b in f_bricks[z]:
        removed = set([b])
        for s in sorted(f_bricks_start):
            if s > z:
                for b1 in f_bricks_start[s]:
                    if fall(b1, f_bricks, removed) != b1:
                        # print(b)
                        chain_count += 1
                        removed.add(b1)
            

print(chain_count)

            