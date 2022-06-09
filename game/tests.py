from django.test import TestCase
from .gameplay.deck import FullDeck, Card, Cards, Value, Suit


class TestDeckandCards(TestCase):
    def setUp(self) -> None:
        self.full_deck = FullDeck()

    def test_full_deck(self):
        deck = FullDeck()
        deck.shuffle()
        print(deck)
        self.assertEqual(len(deck.cards), 52)

    def test_card_from_str(self):
        card = Card.card_from_str("10_spade")
        self.assertEqual(card.value, Value.TEN)
        self.assertEqual(card.suit, Suit.SPADE)

    def test_card_points(self):
        test_cases = [
            {
                "value": Value.ACE,
                "suit": Suit.SPADE,
                "points": 1,
            },
            {
                "value": Value.JACK,
                "suit": Suit.CLUB,
                "points": 10,
            },
            {
                "value": Value.FIVE,
                "suit": Suit.DIAMOND,
                "points": 5,
            },
            {
                "value": Value.KING,
                "suit": Suit.SPADE,
                "points": 10,
            },
        ]
        for case in test_cases:
            card = Card(case["value"], case["suit"])
            self.assertEqual(card.points, case["points"])

    def test_card_equality(self):
        card_1 = Card(Value.SEVEN, Suit.CLUB)
        card_2 = Card(Value.SEVEN, Suit.DIAMOND)
        card_3 = Card(Value.EIGHT, Suit.CLUB)

        self.assertEqual(card_1, card_2)
        self.assert_(card_2 != card_3)

    def test_cards_from_str(self):
        cards_str = "10_spade,5_heart,9_diamond,J_club,A_club"
        cards = Cards.cards_from_str(cards_str)
        self.assertEqual(len(cards), 5)
        self.assertEqual(cards.cards[0], Card(Value.TEN, Suit.SPADE))


class TestState(TestCase):
    pass


class TestPlayer(TestCase):
    pass


class TestRound(TestCase):
    pass
