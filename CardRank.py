from enum import IntEnum


class CardRank(IntEnum):
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 10
    Queen = 10
    King = 10
    Ace = 11

    @staticmethod
    def tens():
        return [CardRank.Ten, CardRank.Jack, CardRank.Queen, CardRank.King]


if __name__ == '__main__':
    for rank in CardRank:
        print(rank)
