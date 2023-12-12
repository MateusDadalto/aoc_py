from dataclasses import dataclass
from collections import Counter
from enum import Enum
path = "day_7.txt"
# path = "test.txt"

class Card(Enum):
    T = 10
    J = 0
    Q = 12
    K = 13
    A = 14

class HandType(Enum):
    HIGH_CARD = 0
    PAIR = 1
    TWO_PAIRS = 2
    TRIO = 3
    FULL_HOUSE = 4
    FOUR = 5
    FIVE = 6

    def __lt__(self, other: object):
        return self.value < other.value
    
    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

@dataclass(init=False, order=False, repr=False)
class Hand:
    cards: list[int]
    original: str
    bid: int
    hand_type: HandType

    def __init__(self, cards:str, bid: int) -> None:
        self.cards = [int(c) if c.isdigit() else Card[c].value for c in cards]
        self.original = cards
        self.bid = bid
        self.__calculate_hand_type()

    def __calculate_hand_type(self):
        c = dict(Counter(self.cards))
        joker_count = 0
        if 0 in c:
            joker_count = c.get(0)
            c.pop(0)

        count = [v for v in c.values()]
        count.sort(reverse=True)

        if joker_count == 5:
            count = [5]
        else:
            count[0] = count[0] + joker_count

        if count == [5]:
            self.hand_type = HandType.FIVE
        elif count == [4, 1]:
            self.hand_type = HandType.FOUR
        elif count == [3, 2]:
            self.hand_type = HandType.FULL_HOUSE
        elif count == [3, 1, 1]:
            self.hand_type = HandType.TRIO
        elif count == [2, 2, 1]:
            self.hand_type = HandType.TWO_PAIRS
        elif count == [2, 1, 1, 1]:
            self.hand_type = HandType.PAIR
        else:
            self.hand_type = HandType.HIGH_CARD

    def __lt__(self, other: object):
        if self.hand_type != other.hand_type:
            return self.hand_type < other.hand_type

        return self.cards < other.cards
    
    def __eq__(self, other: object) -> bool:
        return self.cards == other.cards
    
    def __repr__(self) -> str:
        return f'{self.hand_type} - {self.original} {self.bid}'
    
    

hands = []
with open(path, 'r') as file:
    for line in file:
        cards, bid = line.strip().split()
        hands.append(Hand(cards, int(bid)))

hands.sort()

with open('answer.txt', 'w') as f:
    for item in hands:
        f.write("%s\n" % item)

# print(hands)
answer = [(i+1)*h.bid for i,h in enumerate(hands)]
print(sum(answer))
