path = "day_02.txt"
# path = "test.txt"

def is_safe(arr):
    direction = None
    for i in range(len(arr) - 1):
        a = int(arr[i]) - int(arr[i+1])

        if 1 <= abs(a) <=3:
            if a < 0 and direction != "ASC":
                direction = "DESC"
            elif a > 0 and direction != "DESC":
                direction = "ASC"
            else:
                return False, i
        else:
            return False, i            
    return True, i

with open(path) as f:
    lines = f.readlines()

safe = 0
for l in lines:
    ns = l.split()

    error = None
    r,i = is_safe(ns)

    if r:
        safe += 1
    else:
        damp1, y = is_safe([ns[x] for x in range(len(ns)) if x != i])
        damp2, y = is_safe([ns[x] for x in range(len(ns)) if x != i+1])
        damp3, y = is_safe([ns[x] for x in range(len(ns)) if x != i-1])

        if damp1:
            print("safe damp: ",[ns[x] for x in range(len(ns)) if x != i], l)
            safe += 1
        elif damp2:
            print("safe damp: ",[ns[x] for x in range(len(ns)) if x != i], l)
            safe += 1
        elif damp3:
            print("safe damp: ",[ns[x] for x in range(len(ns)) if x != i-1], l)
            safe += 1

print(safe)
        

 
