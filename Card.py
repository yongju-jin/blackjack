from CardSuit import CardSuit
from CardRank import CardRank


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank.name} of {self.suit.name}'


if __name__ == '__main__':
    two_hearts = Card(CardSuit.Hearts, CardRank.Ace)
    print(two_hearts)
