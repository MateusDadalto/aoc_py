path = "day_2.txt"
# path = "test.txt"

bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

r = {}


def is_valid(draw: str):
    for b in draw.split(', '):
        balls = b.split(' ')

        if int(balls[0]) > bag.get(balls[1]):
            return False

    return True

with open(path, 'r') as file:
    for line in file:
        parts = line.strip().split(': ')
        id = int(parts[0].removeprefix('Game').strip())
        valid = True
        draws = parts[1].split('; ')
        for draw in draws:
            if not is_valid(draw):
                valid = False
                continue
            # balls = { b.split(' ')[1]:b.split(' ')[0] for b in game.split(', ') }

        r[id] = valid
        # print(games)

answer = sum(key for key, value in r.items() if value)
print(answer)