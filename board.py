from dataclasses import dataclass

from move import *


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


def legal_moves(b: Board) -> list[Move]:
    """Return a list of all the legal moves on the given board.
    >>> legal_moves(make_board())
    [Move(source=17, target=13), Move(source=18, target=13), Move(source=19, target=13)]
    """
    free_points = [i for i in range(1, 26) if is_free(i, b)]
    moves = []
    for piece_index in players_pieces(b):
        for i in free_points:
            move = make_move(piece_index, i)
            if is_legal(move, b):
                moves.append(move)
    return moves


def is_legal(m: Move, b: Board) -> bool:
    """Return True if the move m is legal on the given board."""
    dx = displacement_x(m)
    dy = -displacement_y(m) if b.white_plays else displacement_y(m)
    forward_move = dx == 0 and dy == 1
    diagonal_move = on_diagonal(source(m)) and abs(dx) == 1 and dy == 1
    attack = is_attack_move(m) and attack_index(m) in opponents_pieces(b)
    return is_free(target(m), b) and (forward_move or diagonal_move or attack)


def move(m: Move, b: Board) -> None:
    """Update the board to simulate a given move."""
    player = players_pieces(b)
    opponent = opponents_pieces(b)
    player.remove(m.source)
    player.append(m.target)
    if is_attack_move(m):
        opponent.remove(attack_index(m))
    b.white_plays = not b.white_plays


def is_game_over(b: Board) -> bool:
    """Return True if the game is over.
    >>> is_game_over(make_board())
    False
    """
    return not b.black or not b.white or not legal_moves(b)


def copy(b: Board) -> Board:
    """Return a copy of the given board."""
    return Board(list(b.black), list(b.white), b.white_plays)


# Helpers
def is_attack_move(m: Move) -> bool:
    dx = displacement_x(m)
    dy = displacement_y(m)
    return ((abs(dx) == 2 and dy == 0 or dx == 0 and abs(dy) == 2)
            or (on_diagonal(source(m)) and abs(dx) == 2 and abs(dy) == 2))


def on_diagonal(i: int) -> bool:
    return i % 2 == 1


def is_free(i: int, b: Board) -> bool:
    return i not in b.white and i not in b.black


def players_pieces(b: Board) -> list[int]:
    return b.white if b.white_plays else b.black


def opponents_pieces(b: Board) -> list[int]:
    return b.black if b.white_plays else b.white


def attack_index(m: Move) -> int:
    return (source(m) + target(m)) // 2


def displacement_x(m: Move) -> int:
    return column(target(m)) - column(source(m))


def displacement_y(m: Move) -> int:
    return row(target(m)) - row(source(m))


def row(i: int) -> int:
    return (i-1) // 5 + 1


def column(i: int) -> int:
    return (i-1) % 5 + 1
