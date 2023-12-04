path = "day_4.txt"
# path = "test.txt"

# Will store card relevant data here
cards = {}

def calculate_total(card):
    """
    card total means how many cards it will give you in the end (including itself)
    """
    # if the card has a total, return this total
    if card['total']:
        return card['total']

    # when a card has no total we need to calculate it
    # we start by setting total = 1 (its own value)
    total = 1
    # then we check the total of its "children cards"
    # they should already be defined because we are calculating totals from bottom to top
    prizes = card['cards_won']
    for c in prizes:
        total += calculate_total(cards[c])

    card['total'] = total
    return total


# I'm justing "parsing" the cards here
with open(path, 'r') as file:
    for line in file:
        # ["card X", "a b c | i j k"]
        line = line.strip().split(':')
        card_id = int(line[0].removeprefix('Card').strip())
        # ["a b c", "i j k"]
        scratch_info = line[1].split('|')
        # [a, b, c]
        winning_numbers = [
            int(n) for n in scratch_info[0].strip().replace('  ', ' ').split(' ')]
        # [i, j, k]
        player_numbers = [
            int(n) for n in scratch_info[1].strip().replace('  ', ' ').split(' ')]

        # get the cards intersection and then the cards won
        intersection = [a for a in player_numbers if a in winning_numbers]
        cards_won = [n for n in range(
            card_id + 1, card_id + len(intersection) + 1)]

        cards[card_id] = {
            # if the card gives no other card than its value is 1
            # otherwise we will calculate it later ;D
            'total': None if len(cards_won) > 0 else 1,
            'cards_won': cards_won
        }

inventory = 0
# the key of this code is here, we go from the last card to the first one
# because the card links only go one way (card 1 gives card 2 but 2 never gives 1)
# you can save a lot of time doing this in reverse
# calculating first the independent cards and then the dependent cards
for i in range(1, card_id + 1).__reversed__():
    inventory += calculate_total(cards[i])

print(inventory)
