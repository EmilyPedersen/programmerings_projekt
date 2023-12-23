from dataclasses import dataclass
from functools import reduce

from board import *
from move import *


def next_move(b: Board, depth: int = 3) -> Move:
    """Return the best move for the next player.
    Find this by building a minimax tree with the given board and depth.
    """
    t = make_tree(b, depth)
    rate_tree(t)
    max_node = reduce(lambda mn, n: n if n.value > mn.value else mn,
                      t.children)
    return max_node.move


@dataclass
class Tree:
    children: list['Node']
    board: Board
    depth: int


@dataclass
class Node:
    children: list['Node']
    board: Board
    move: Move
    value: float


def make_tree(b: Board, depth: int) -> Tree:
    """Make a new minimax tree with the given board and depth."""


def make_node(b: Board, move: Move, depth: int) -> Node:
    """Make a new node (and its children) where
    move has been made on the given board with depth.
    """


def rate_tree(t: Tree) -> None:
    """Rate all the nodes in the tree."""


def rate_node(n: Node, layer: int, white_player: bool) -> float:
    """Rate a node and all its children.
    Return the value that a parent would have.
    The layer is used to determine whether
    the node is a min or max node.
    """


def rate_board(b: Board, white_player: bool) -> float:
    """Return a value telling how good
    the given board is for the current player.
    This is our heuristic.
    """
    players = b.white if white_player else b.black
    opponents = b.black if white_player else b.white
    # Vi burde nok få den til at undgå uafgjorte kampe.
    return len(players) / len(opponents) if len(opponents) > 0 else 100
