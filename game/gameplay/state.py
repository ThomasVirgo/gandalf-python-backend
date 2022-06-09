from __future__ import annotations

from dataclasses import dataclass
from .player import Player
from .deck import Cards


@dataclass
class GameState:
    players: list[Player]
    turn: Player
    is_slap: bool
    is_gandalf: bool
