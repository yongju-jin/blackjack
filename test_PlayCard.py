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
    hearts_eight = Card(CardSuit.Hearts, CardRank.Eight)

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
        self.assertTrue(play_card.is_black_jack())

    def test_is_not_black_jack_include_ace(self):
        play_card = PlayCard([self.hearts_ace, self.hearts_nine])
        self.assertFalse(play_card.is_black_jack())

    def test_is_not_black_jack_exclude_ace(self):
        play_card = PlayCard([self.hearts_two, self.hearts_nine])
        self.assertFalse(play_card.is_black_jack())

    def test_open_first_card(self):
        first_card = self.hearts_nine
        play_card = PlayCard([first_card, self.hearts_two])
        open_card = play_card.open_first_card()
        self.assertEqual(first_card, open_card)

    def test_add_card(self):
        play_card = PlayCard([self.hearts_two, self.hearts_nine])
        play_card.add_card(self.hearts_ace)
        self.assertTrue(self.hearts_ace in play_card.cards)

    def test_is_burst_false(self):
        play_card = PlayCard([self.hearts_two, self.hearts_nine])
        self.assertFalse(play_card.is_burst())

    def test_is_burst_true(self):
        play_card = PlayCard([self.hearts_ten, self.hearts_nine])
        play_card.add_card(self.hearts_eight)
        self.assertTrue(play_card.is_burst())
