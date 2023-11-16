from dataclasses import dataclass

@dataclass
class Move:
	source: int
	target: int
	
def make_move(scr: int, trg: int) -> Move:
    """Return a move between the two indicies 
    >>> make_move()"""
    return Move(scr, trg)
