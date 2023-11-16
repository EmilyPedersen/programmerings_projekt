from dataclasses import dataclass

@dataclass
class Board:
    black: list[int]
    white: list[int]
    white_plays: bool

def make_board() -> Board:
    """Make a new board where the pieces are at their starting points. 
    """
    Board(range(1,13), range(14,26), True)

