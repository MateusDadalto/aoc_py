path = "day_02.txt"
# path = "test.txt"



with open(path) as f:
    lines = f.readlines()

safe = 0
for l in lines:
    ns = l.split()

    direction = None
    is_safe = True
    for i in range(len(ns) - 1):
        
        a = int(ns[i]) - int(ns[i+1])

        if 1 <= abs(a) <=3:
            if a < 0 and direction != "ASC":
                direction = "DESC"
            elif a > 0 and direction != "DESC" and 1 <= abs(a) <=3:
                direction = "ASC"
            else:
                is_safe = False
        else:
            is_safe = False

    if is_safe:
        safe += 1

print(safe)
        

 
