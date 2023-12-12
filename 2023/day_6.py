from math import sqrt

path = "day_6.txt"
# path = "test.txt"

with open(path, 'r') as file:
    lines = file.readlines()

    time = int(''.join(lines[0].removeprefix('Time:').split()))
    goal = int(''.join(lines[1].removeprefix('Distance:').split()))


# so, the smart way to think about it is to think of the inequation: hold * (Total_time - hold) > goal
# and find the roots of the quadratic equation: -hold**2 + T*hold - goal > 0
def achieve_goal(race):
    time, goal = race
    
    discriminant = sqrt((time**2) - (4*-1*-goal))

    # find two solutions
    root1 = int((-time - discriminant) / (2 * -1))
    root2 = int((-time + discriminant) / (2 * -1))

    return abs(root1 - root2)

r = achieve_goal((time, goal))

print(r)