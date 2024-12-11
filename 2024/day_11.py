from collections import deque
from functools import cache

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
p1_stones = stones
for i in range(blinks):
    after_blink = []
    for stone in p1_stones:
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

    p1_stones = after_blink

print(len(p1_stones))

# Dynamic programming... I need to build intuition for it

def cache_notify(func):
    func = cache(func)
    def notify_wrapper(*args, **kwargs):
        stats = func.cache_info()
        hits = stats.hits
        print(f"INFO: {func.__name__}{args} call")
        results = func(*args, **kwargs)
        stats = func.cache_info()
        if stats.hits > hits:
            print(f"DEBUG: {func.__name__}{args} results hit cached data")
        else:
            print(f"DEBUG:  {func.__name__}{args} results have been cached")
        return results
    return notify_wrapper

@cache_notify
def count_stone(stone, n):
    # print(stone, n)
    if n == 0:
        return 1

    if stone == 0:
        return count_stone(1, n-1)
    elif len(str(stone))%2 == 0:
        stone_str = str(stone)

        part_1 = int(stone_str[:len(stone_str)//2])
        part_2 = int(stone_str[len(stone_str)//2:])
        return count_stone(part_1, n-1) + count_stone(part_2, n-1)
    else:
        return count_stone(stone * 2024, n-1)

print(sum([count_stone(s, 75) for s in stones]))