from CardSuit import CardSuit
from Card import Card
from CardRank import CardRank


class PlayCard:
    def __init__(self, cards: list):
        if len(cards) != 2:
            raise AssertionError

        if cards[0] == cards[1]:
            raise AssertionError

        self.cards = cards

    def __str__(self):
        ret = ''
        for card in self.cards:
            ret += f'{card}\n'
        return ret

    def is_black_jack(self) -> bool:
        ranks = list(map(lambda card: card.rank, self.cards))
        ranks.sort()
        print(ranks)
        if CardRank.Ace in ranks:
            return ranks[0] in CardRank.tens()
        else:
            return False


if __name__ == '__main__':
    playCard = PlayCard([Card(CardSuit.Hearts, CardRank.Ace), Card(CardSuit.Clover, CardRank.Jack)])
    print(playCard)
