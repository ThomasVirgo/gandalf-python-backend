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


class Card:
    def __init__(self, value: Value, suit: Suit) -> None:
        self.value = value
        self.suit = suit

    def __repr__(self) -> str:
        return f"Card(value={self.value.name}, suit={self.suit.name})"

    @classmethod
    def card_from_str(cls, card_str: str):
        value_map = {
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

        suit_map = {
            "diamond": Suit.DIAMOND,
            "heart": Suit.HEART,
            "club": Suit.CLUB,
            "spade": Suit.SPADE,
        }

        value, suit = card_str.split("_")  # example string --> 10_spade

        return cls(value_map[value], suit_map[suit])

    @property
    def points(self) -> int:
        picture_cards = {Value.JACK, Value.QUEEN, Value.KING}
        if self.value in picture_cards:
            return 10
        return self.value.value

    def __eq__(self, other: Card) -> bool:
        return self.value == other.value


class FullDeck:
    def __init__(self) -> None:
        self.cards = [Card(v, s) for s in Suit for v in Value]

    def __len__(self):
        return len(self.cards)

    def __str__(self) -> str:
        return f"Full deck -> {len(self.cards)} cards"

    def shuffle(self):
        shuffle(self.cards)


class Cards:
    def __init__(self, cards: list[Card]) -> None:
        self.cards = cards