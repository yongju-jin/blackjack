from unittest import TestCase

from Card import Card
from CardRank import CardRank
from CardSuit import CardSuit


class TestCard(TestCase):

    def test_equals(self):
        self.assertEqual(Card(CardSuit.Hearts, CardRank.Ace), Card(CardSuit.Hearts, CardRank.Ace))

    def test_add(self):
        ret = Card(CardSuit.Hearts, CardRank.Ten) + Card(CardSuit.Hearts, CardRank.Five)
        self.assertEqual(15, ret)