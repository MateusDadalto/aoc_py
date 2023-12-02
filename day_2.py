path = "day_2.txt"
# path = "test.txt"

games = {}


def set_min_bag(draw: str, bag: dict[str, int]):
    for b in draw.split(', '):
        balls = b.split(' ')
        qty = int(balls[0])
        if qty > bag.get(balls[1]):
            bag[balls[1]] = qty


with open(path, 'r') as file:
    for game in file:
        colors = ['red', 'green', 'blue']
        bag = {color: 0 for color in colors}

        parts = game.strip().split(': ')
        game_id = int(parts[0].removeprefix('Game').strip())
        draws = parts[1].split('; ')
        for draw in draws:
            set_min_bag(draw, bag)

        games[game_id] = bag

answer = sum(bag.get('red', 1) * bag.get('blue', 1) *
             bag.get('green', 1) for bag in games.values())

print(answer)
