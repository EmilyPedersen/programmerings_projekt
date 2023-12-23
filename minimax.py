from dataclasses import dataclass

from board import *
from move import *


def next_move(b: Board, depth: int = 3) -> Move:
    """Return the best move for the next player.
    Find this by building a minimax tree with the given board and depth.
    """
    return legal_moves(b)[0]


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
    value: int


def make_tree(b: Board, depth: int) -> Tree:
    """Make a new minimax tree with the given board and depth."""


def make_node(b: Board, move: Move, depth: int) -> Node:
    """Make a new node (and its children) where
    move has been made on the given board with depth.
    """


def rate_tree(t: Tree) -> None:
    """Rate all the nodes in the tree."""


def rate_node(n: Node, layer: int) -> int:
    """Rate a node and all its children.
    Return the value that a parent would have.
    The layer is used to determine whether
    the node is a min or max node.
    """


def rate_board(b: Board) -> int:
    """Return a value telling how good
    the given board is for the current player.
    This is our heuristic.
    """
