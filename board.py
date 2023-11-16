from dataclasses import dataclass

@dataclass
class Board:
    black: list[int]
    white: list[int]
    white_plays: bool



