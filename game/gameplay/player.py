from dataclasses import dataclass
from .deck import Cards


@dataclass
class Player:
    id: int
    first_name: str
    last_name: str
    is_turn: bool
    cards: Cards
    score: int
    games_played: int

    def start_turn(self):
        self.is_turn = True

    def end_turn(self):
        self.is_turn = False

    def calculate_score(self):
        score = 0
        for c in self.cards:
            score += c.points
        self.score = score
        return score
