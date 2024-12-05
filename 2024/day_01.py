path = "day_01.txt"
path = "test.txt"

with open(path) as f:
    lines = f.readlines()

left_col = []
right_col = []

for line in lines:
    l,result_1 = line.split()
    left_col.append(int(l))
    right_col.append(int(result_1))


result_1 = 0

left_col.sort()
right_col.sort()

for i,j in zip(left_col,right_col):
     result_1 += abs(i-j)

print("Part 1:", result_1)

# 2
similarity = []
for i in left_col:
    similarity.append(i*right_col.count(i))

print("Part 2:", sum(similarity))