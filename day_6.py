path = "day_6.txt"
# path = "test.txt"

with open(path, 'r') as file:
    lines = file.readlines()

    time = int(''.join(lines[0].removeprefix('Time:').split()))
    goal = int(''.join(lines[1].removeprefix('Distance:').split()))
    
def achieve_goal(race):
    time, goal = race
    counter = 0
    for i in range(1, time + 1):
        time_held = i
        speed = time_held
        distance = (time - time_held)*speed

        if distance > goal:
            counter += 1

    return counter

r = achieve_goal((time, goal))

print(r)