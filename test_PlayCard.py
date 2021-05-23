from unittest import TestCase

from CardRank import CardRank
from CardSuit import CardSuit
from PlayCard import PlayCard
from Card import Card


class TestPlayCard(TestCase):
    hearts_ace = Card(CardSuit.Hearts, CardRank.Ace)
    hearts_ten = Card(CardSuit.Hearts, CardRank.Ten)
    hearts_nine = Card(CardSuit.Hearts, CardRank.Nine)
    hearts_two = Card(CardSuit.Hearts, CardRank.Two)

    def test_constructor_success(self):
        PlayCard([self.hearts_ace, self.hearts_ten])

    def test_constructor_with_error_more_than_two_cards(self):
        try:
            play_card = PlayCard([self.hearts_ace, self.hearts_ten, self.hearts_nine])
        except AssertionError:
            pass
        else:
            self.fail('ExpectedException not raised')

    def test_constructor_with_error_same_card(self):
        try:
            play_card = PlayCard([Card(CardSuit.Hearts, CardRank.Ace), Card(CardSuit.Hearts, CardRank.Ace)])
        except AssertionError:
            pass
        else:
            self.fail('ExpectedException not raised')

    def test_is_black_jack(self):
        play_card = PlayCard([self.hearts_ace, self.hearts_ten])
        print(play_card)
        self.assertTrue(play_card.is_black_jack())

    def test_is_not_black_jack_include_ace(self):
        play_card = PlayCard([self.hearts_ace, self.hearts_nine])
        print(play_card)
        self.assertFalse(play_card.is_black_jack())

    def test_is_not_black_jack_exclude_ace(self):
        play_card = PlayCard([self.hearts_two, self.hearts_nine])
        print(play_card)
        self.assertFalse(play_card.is_black_jack())

