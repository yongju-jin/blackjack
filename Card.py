from dataclasses import dataclass

from CardSuit import CardSuit
from CardRank import CardRank


@dataclass(init=True, repr=True, eq=True)
class Card:

    suit: CardSuit
    rank: CardRank

    def __str__(self):
        return f'{self.rank.name} of {self.suit.name}'


if __name__ == '__main__':
    two_hearts = Card(CardSuit.Hearts, CardRank.Ace)
    print(two_hearts)
