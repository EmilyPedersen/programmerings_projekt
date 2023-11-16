from dataclasses import dataclass


@dataclass
class Board:
    black: list[int]
    white: list[int]
    white_plays: bool


def make_board() -> Board:
    """Make a new board where the pieces are at their starting points. 
    """
    return Board(list(range(1, 13)), list(range(14, 26)), True)

