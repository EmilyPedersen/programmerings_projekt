from dataclasses import dataclass


@dataclass
class Board:
    black: list[int]
    white: list[int]
    white_plays: bool


def make_board() -> Board:
    """Make a new board where the pieces are at their starting points.
    >>> make_board()
    Board(black=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], white=[14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], white_plays=True)
    """
    return Board(list(range(1, 13)), list(range(14, 26)), True)


def white_plays(b: Board) -> bool:
    """Return True if it is whites turn.
    >>> white_plays(make_board())
    True
    """
    return b.white_plays


def black(b: Board) -> list[int]:
    """Return a list containing the indexes of all
    the points where there are black pieces on the board.
    >>> black(make_board())
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    """
    return b.black


def white(b: Board) -> list[int]:
    """Return a list containing the indexes of all
    the points where there are white pieces on the board.
    >>> white(make_board())
    [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    """
    return b.white
