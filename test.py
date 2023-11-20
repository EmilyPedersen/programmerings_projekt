import doctest

import board as board_module
import move as move_module

from board import *
from move import *

# Running doctest
doctest.testmod(board_module)
doctest.testmod(move_module)


# Testing the game
def move_list(moves: list[tuple[int, int]]) -> list[Move]:
    return [make_move(source, target) for (source, target) in moves]


b = make_board()

# The black, white, and legal_moves might need to be sorted.
assert white_plays(b)
assert black(b) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
assert white(b) == [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
assert legal_moves(b) == move_list([(17, 13), (18, 13), (19, 13)])
assert not is_game_over(b)

move(make_move(18, 13), b)

assert not white_plays(b)
assert black(b) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
assert white(b) == [14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 13]
assert legal_moves(b) == move_list([(8, 18)])
assert not is_game_over(b)

move(make_move(8, 18), b)

assert white_plays(b)
assert black(b) == [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 18]
assert white(b) == [14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25]
assert legal_moves(b) == move_list([(17, 13), (19, 13), (23, 13)])
assert not is_game_over(b)

move(make_move(23, 13), b)

assert not white_plays(b)
assert black(b) == [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12]
assert white(b) == [14, 15, 16, 17, 19, 20, 21, 22, 24, 25, 13]
assert legal_moves(b) == move_list([(3, 8)])
assert not is_game_over(b)

move(make_move(3, 8), b)

assert white_plays(b)
assert black(b) == [1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 8]
assert white(b) == [14, 15, 16, 17, 19, 20, 21, 22, 24, 25, 13]
assert legal_moves(b) == move_list([(13, 3), (15, 3)])
assert not is_game_over(b)

move(make_move(15, 3), b)

assert not white_plays(b)
assert black(b) == [1, 2, 4, 5, 6, 7, 10, 11, 12, 8]
assert white(b) == [14, 16, 17, 19, 20, 21, 22, 24, 25, 13, 3]
assert legal_moves(b) == move_list([(14, 9), (20, 15)])
assert not is_game_over(b)
