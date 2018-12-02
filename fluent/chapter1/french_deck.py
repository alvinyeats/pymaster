# _*_ coding: utf-8 _*_

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]


if __name__ == "__main__":
    beer_card = Card('7', 'diamond')
    print(beer_card)

    deck = FrenchDeck()
    print(len(deck))
    print(deck[1])
    print(type(deck))
    print(type(deck[1]))
    print(FrenchDeck.__bases__)
    print(Card.__bases__)



