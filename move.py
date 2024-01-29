from dataclasses import dataclass


@dataclass
class Move:
    source: int
    target: int


def make_move(scr: int, trg: int) -> Move:
    """Return a move between the two indicies. 
    Requires: 1 <= src <= 25 and 1 <= trg <= 25
    >>> make_move(13, 8)
    Move(source=13, target=8)
    """
    return Move(scr, trg)


def source(m: Move) -> int:
    """Return the source point.
    >>> source(make_move(13, 8))
    13
    """
    return m.source


def target(m: Move) -> int:
    """Return the target point.
    >>> target(make_move(13, 8))
    8
    """
    return m.target
