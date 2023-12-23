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
    new_board = copy(b)
    children = []
    for legal_move in legal_moves(new_board):
        child_node = make_node(new_board, legal_move, depth-1)
        children.append(child_node)
    return Tree(children, b, depth)


def make_node(b: Board, m: Move, depth: int) -> Node:
    """Make a new node (and its children) where
    move has been made on the given board with depth.
    """
    new_board = copy(b)
    move(m, new_board)
    children = []
    if depth > 0 and not is_game_over(new_board):
        for legal_move in legal_moves(new_board):
            child_node = make_node(new_board, legal_move, depth-1)
            children.append(child_node)
    return Node(children, new_board, m, -1)


def rate_tree(t: Tree) -> None:
    """Rate all the nodes in the tree."""
    for child in t.children:
        rate_node(child, 1, white_plays(t.board))


def rate_node(n: Node, layer: int, white_player: bool) -> None:
    """Rate a node and all its children.
    Return the value that a parent would have.
    The layer is used to determine whether
    the node is a min or max node.
    """
    if n.children == []:
        n.value = rate_board(n.board, white_player)
    else:
        values = []
        for child in n.children:
            rate_node(child, layer + 1, white_player)
            values.append(child.value)

        if layer % 2 == 1:
            n.value = reduce(lambda x, y: y if y < x else x, values, values[0])

        else:
            n.value = reduce(lambda x, y: y if y > x else x, values, values[0])


def rate_board(b: Board, white_player: bool) -> float:
    """Return a value telling how good
    the given board is for the current player.
    This is our heuristic.
    """
    players = b.white if white_player else b.black
    opponents = b.black if white_player else b.white
    # Vi burde nok få den til at undgå uafgjorte kampe.
    return len(players) / len(opponents) if len(opponents) > 0 else 100
