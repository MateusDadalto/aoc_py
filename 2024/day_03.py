import re

path = "day_03.txt"
# path = "test.txt"

def parse_mul(s:str):
    first_number = s[s.index("(")+1:s.index(",")]
    second_number = s[s.index(",")+1:-1]

    return int(first_number) * int(second_number)

with open(path) as f:
    # will treat everything as a single string since each new line does not reset the state of the DOs and DON'Ts
    lines = f.read()


#### PART 1 #####
p1 = 0
for i in re.findall(r"mul\(\d+,\d+\)", lines):
    p1 += parse_mul(i)

print("p1: ", p1)

##### PART 2 #####

# First split the sections into DO sections 
# it may contain don't in it but I'm sure they will start with DO()
# From the example: ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)un", "mul(8,5))"]
dos = lines.split("do()")

# For each DO section split it in sub-sections on every don't
# the first section will be DO, the others will be DON'T
# From the example: [["xmul(2,4)&mul[3,7]!^","_mul(5,5)+mul(32,64](mul(11,8)un"], ["mul(8,5))"]]
#                       /\ FIRST IS DO           OTHERS ARE /\ DONT                 /\ FIRST IS DO
do_then_dont = [i.split("don't()") for i in dos]

p2 = 0
for do_and_donts in do_then_dont:
    # First is DO
    do = do_and_donts[0]
    for i in re.findall(r"mul\(\d+,\d+\)", do):
        p2 += parse_mul(i)
    
print("p2: ", p2)
