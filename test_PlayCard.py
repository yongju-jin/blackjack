from unittest import TestCase

from CardRank import CardRank
from CardSuit import CardSuit
from PlayCard import PlayCard
from Card import Card


class TestPlayCard(TestCase):

    def test_is_black_jack(self):
        black_jack = PlayCard([Card(CardSuit.Hearts, CardRank.Ace), Card(CardSuit.Hearts, CardRank.Ten)])
        print(black_jack)
        self.assertTrue(black_jack.is_black_jack())

    def test_is_not_black_jack_include_ace(self):
        black_jack = PlayCard([Card(CardSuit.Hearts, CardRank.Ace), Card(CardSuit.Hearts, CardRank.Nine)])
        print(black_jack)
        self.assertFalse(black_jack.is_black_jack())

    def test_is_not_black_jack_exclude_ace(self):
        black_jack = PlayCard([Card(CardSuit.Hearts, CardRank.Two), Card(CardSuit.Hearts, CardRank.Nine)])
        print(black_jack)
        self.assertFalse(black_jack.is_black_jack())
