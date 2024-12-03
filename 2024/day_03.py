import re

path = "day_03.txt"
# path = "test.txt"

def parse_mul(s:str):
    first_number = s[s.index("(")+1:s.index(",")]
    second_number = s[s.index(",")+1:-1]

    # print(first_number)
    # print(second_number)
    return int(first_number) * int(second_number)

with open(path) as f:
    lines = f.readlines()

total = 0

for line in lines:
    for i in re.findall(r"mul\(\d+,\d+\)", line):
        
        total += parse_mul(i)

print("p1: ", total)
