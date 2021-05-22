from typing import Any, Union

from Card import Card
from CardRank import CardRank
from CardSuit import CardSuit
import random


class Deck:
    def __init__(self):
        self.cards = []
        self.__add_card()

    def __add_card(self):
        cards = []
        for suit in CardSuit:
            for rank in CardRank:
                cards.append(Card(suit, rank))
        random.shuffle(cards)
        self.cards = self.cards + cards


if __name__ == '__main__':
    dealer = Deck()
    print(dealer.cards)
