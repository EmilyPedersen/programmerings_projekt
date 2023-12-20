from board import *
from move import *


def next_move(b: Board, depth: int = 3) -> Move:
    """Return the best move for the next player.
    Find this by building a minimax tree with the given board and depth.
    """
    return legal_moves(b)[0]
