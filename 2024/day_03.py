import re

path = "day_03.txt"
# path = "test.txt"

def parse_mul(s:str):
    first_number = s[s.index("(")+1:s.index(",")]
    second_number = s[s.index(",")+1:-1]

    return int(first_number) * int(second_number)

def start_disabled(s:str):
    return s.startswith(s.split("don't()")[0])

with open(path) as f:
    lines = f.read()

total = 0

toggle_sections = []
dos = lines.split("do()")
do_then_dont = [i.split("don't()") for i in dos]
for do in do_then_dont:
    status = True
    for section in do:
        # print(section, status)
        if status:
            for i in re.findall(r"mul\(\d+,\d+\)", section):
                if status:
                    total += parse_mul(i)
    
        status = False
    

print("p2: ", total)
