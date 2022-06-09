from __future__ import annotations
import enum
from random import shuffle


class Value(enum.Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Suit(enum.Enum):
    DIAMOND = "diamond"
    HEART = "heart"
    CLUB = "club"
    SPADE = "spade"


VALUE_MAP = {
    "A": Value.ACE,
    "2": Value.TWO,
    "3": Value.THREE,
    "4": Value.FOUR,
    "5": Value.FIVE,
    "6": Value.SIX,
    "7": Value.SEVEN,
    "8": Value.EIGHT,
    "9": Value.NINE,
    "10": Value.TEN,
    "J": Value.JACK,
    "Q": Value.QUEEN,
    "K": Value.KING,
}

SUIT_MAP = {
    "diamond": Suit.DIAMOND,
    "heart": Suit.HEART,
    "club": Suit.CLUB,
    "spade": Suit.SPADE,
}


class Card:
    def __init__(self, value: Value, suit: Suit) -> None:
        self.value = value
        self.suit = suit
        self.card_position = None
        self.face_up = False

    def assign_card_position(self, pos):
        self.card_position = pos

    def __repr__(self) -> str:
        return f"Card(value={self.value.name}, suit={self.suit.name})"

    def __eq__(self, other: Card) -> bool:
        return self.value == other.value

    @classmethod
    def card_from_str(cls, card_str: str):
        value, suit = card_str.split("_")  # example string --> 10_spade

        return cls(VALUE_MAP[value], SUIT_MAP[suit])

    @property
    def points(self) -> int:
        picture_cards = {Value.JACK, Value.QUEEN, Value.KING}
        if self.value in picture_cards:
            return 10
        return self.value.value

    def turn_over(self):
        self.face_up = True


class FullDeck:
    def __init__(self) -> None:
        self.cards = [Card(v, s) for s in Suit for v in Value]

    def __len__(self):
        return len(self.cards)

    def __str__(self) -> str:
        sum_str = ""
        for c in self.cards:
            sum_str += f"{c.value.name} of {c.suit.name} \n"
        return sum_str

    def shuffle(self):
        shuffle(self.cards)


class Cards:
    def __init__(self, cards: list[Card]) -> None:
        self.cards = cards

    def __len__(self):
        return len(self.cards)

    @classmethod
    def cards_from_str(cls, str):
        """str should be of the form "10_spade,5_heart,6_diamond" ...."""
        card_strs = str.split(",")
        cards = []
        for s in card_strs:
            value, suit = s.split("_")
            cards.append(Card(VALUE_MAP[value], SUIT_MAP[suit]))
        return cls(cards)


class Deck:
    def __init__(self, cards: list[Card]) -> None:
        self.cards = cards

    def deck_from_str(cls, cards_str: str):
        pass


class FaceDownDeck(Deck):
    def create_initial_deck(self):
        pass


class FaceUpDeck(Deck):
    pass
