path = "day_2.txt"
# path = "test.txt"


r = {}

def set_min_bag(draw: str, bag: dict[str, int]):
    for b in draw.split(', '):
        balls = b.split(' ')
        qty = int(balls[0])
        if qty > bag.get(balls[1]):
            bag[balls[1]] = qty
    
with open(path, 'r') as file:
    for game in file:
        bag = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        parts = game.strip().split(': ')
        id = int(parts[0].removeprefix('Game').strip())
        valid = True
        draws = parts[1].split('; ')
        for draw in draws:
            set_min_bag(draw, bag)
            # balls = { b.split(' ')[1]:b.split(' ')[0] for b in game.split(', ') }

        r[id] = bag
        # print(games)

answer = sum(bag.get('red', 1) * bag.get('blue', 1) * bag.get('green', 1) for bag in r.values())

print(answer)