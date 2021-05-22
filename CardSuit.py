from enum import Enum


class CardSuit(Enum):
    Clover = 1
    Hearts = 2
    Diamond = 3
    Spades = 4


if __name__ == '__main__':
    for suit in CardSuit:
        print(suit)