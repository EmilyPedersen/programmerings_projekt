from board import Board, legal_moves
from move import Move

def next_move(b: Board, n: int = 3) -> Move:
    """Returns the next move for the autoplayer."""
    return legal_moves(b)[0]
