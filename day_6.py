path = "day_6.txt"
# path = "test.txt"

with open(path, 'r') as file:
    lines = file.readlines()

    time = [int(t) for t in lines[0].removeprefix('Time:').split()]
    goal = [int(d) for d in lines[1].removeprefix('Distance:').split()]
    
races = zip(time, goal)

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

r = 1
for race in races:
    r *= achieve_goal(race)

print(r)