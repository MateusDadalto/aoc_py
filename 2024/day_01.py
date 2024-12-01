path = "day_01.txt"

with open("day_01.txt") as f:
    a = f.readlines()

    pairs = []
    for l in a:
        numbers = []
        acc = ""
        for c in l:
            if c.isnumeric():
                acc += c
            elif len(acc) > 0:
                numbers.append(int(acc))
                acc = ""
        
        pairs.append(numbers)
    
    x = [i for i,j in pairs]
    y = [j for i,j in pairs]

    # x.sort()
    # y.sort()

r = 0

# 1
# for i,j in zip(x,y):
#     r += abs(i-j)

# print(r)

# 2
m = []
for i in x:
    m.append(i*y.count(i))
    # print(y.count(i))

# print(m)

n = []
for j in y:
    n.append(j*x.count(j))

# print(n)

print(sum(m))