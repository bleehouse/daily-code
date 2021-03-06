# 전문가를 위한 파이썬(Fluent Python) example 1-1 일련의 카드로 구성한 카드 한벌

import collections
from random import choice


Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __reversed__(self):
        return reversed(self._cards)


beer_card = Card('7', 'diamonds')

print(beer_card)

deck = FrenchDeck()
print(deck.ranks)
print(deck.suits)
print(len(deck))
print(deck[10])
print(deck._cards)
print(choice(deck))
print(deck[:3])

for card in deck: # doctest: +ELIPSIS
    print(card)

for card in reversed(deck):  # doctest: +ELIPSIS
    print('------------') # 특별 메소드를 변경해 볼 수 있다.
    print(card)
