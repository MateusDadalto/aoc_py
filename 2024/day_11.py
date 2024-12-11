from collections import deque

path = "day_11.txt"
# path = "test.txt"

directions = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

with open(path) as f:
    stones = [int(s) for s in f.read().strip().split()]

blinks = 25
for i in range(blinks):
    after_blink = []
    print(i, end='\r')
    for stone in stones:
        if stone == 0:
            after_blink.append(1)
        elif len(str(stone))%2 == 0:
            stone_str = str(stone)

            part_1 = int(stone_str[:len(stone_str)//2])
            part_2 = int(stone_str[len(stone_str)//2:])
            after_blink.append(part_1)
            after_blink.append(part_2)
        else:
            after_blink.append(stone * 2024)

    stones = after_blink
print(i)
print(len(stones))