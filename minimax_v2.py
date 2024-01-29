from dataclasses import dataclass
from functools import reduce

from board import *
from move import *


def next_move(b: Board, depth: int = 3) -> Move:
    """Return the best move for the next player.
    Find this by building a minimax tree with the given board and depth.
    Requires: depth > 0
    """
    root = make_tree(b, None, depth)
    rate_tree(root, white_plays(b))
    return _max_node(root.children).move


@dataclass
class Node:
    children: list['Node']
    board: Board
    move: Move
    value: float


def make_tree(b: Board, m: Move, depth: int) -> Node:
    """Make a tree recursively and return the root node.
    Each node will have a child for each legal move on its board.
    The trees depth is equal to the argument depth.
    """
    children = []
    if depth > 0:
        for legal_move in legal_moves(b):
            child_board = copy(b)
            move(legal_move, child_board)
            child_node = make_tree(child_board, legal_move, depth-1)
            children.append(child_node)
    return Node(children, b, m, 0)


def rate_tree(n: Node, white_player: bool) -> None:
    """Rate a node and all its children recursively."""
    if n.children == []:
        n.value = rate_board(n.board, white_player)
    else:
        for child in n.children:
            rate_tree(child, white_player)

        if white_player == white_plays(n.board):
            n.value = _max_node(n.children).value
        else:
            n.value = _min_node(n.children).value


def rate_board(b: Board, white_player: bool) -> float:
    """Return a value telling how good
    the given board is for the current player.
    This is our heuristic.
    """
    players = white(b) if white_player else black(b)
    opponents = black(b) if white_player else white(b)
    return len(players) - len(opponents)
    # ratio = len(players) / len(opponents) if len(opponents) > 0 else 100 * len(players)
    # if _is_tie(b):
    #     return 1 / ratio
    # else:
    #     return ratio


def _is_tie(b: Board) -> bool:
    """Return true if the game is a tie and false otherwise."""
    return is_game_over(b) and black(b) != [] and white(b) != []


def _max_node(nodes: list[Node]) -> Node:
    """Return the node with the greatest value."""
    return reduce(lambda mn, n: n if n.value > mn.value else mn, nodes)


def _min_node(nodes: list[Node]) -> Node:
    """Return the node with the smallest value."""
    return reduce(lambda mn, n: n if n.value < mn.value else mn, nodes)
