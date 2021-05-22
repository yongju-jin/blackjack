from typing import Any, Union

from Card import Card
from CardRank import CardRank
from CardSuit import CardSuit
import random


class Deck:
    def __init__(self):
        self.cards = []
        for suit in CardSuit:
            for rank in CardRank:
                self.cards.append(Card(suit, rank))
        random.shuffle(self.cards)


if __name__ == '__main__':
    dealer = Deck()
    print(dealer.cards)
