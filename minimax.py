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
    return max_node(t.children).move


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
        rate_node(child, white_plays(t.board))


def rate_node(n: Node, white_player: bool) -> None:
    """Rate a node and all its children."""
    if n.children == []:
        n.value = rate_board(n.board, white_player)
    else:
        for child in n.children:
            rate_node(child, white_player)

        if white_plays(n.board) and white_player:
            n.value = max_node(n.children).value
        else:
            n.value = mini_node(n.children).value


def rate_board(b: Board, white_player: bool) -> float:
    """Return a value telling how good
    the given board is for the current player.
    This is our heuristic.
    """
    players = b.white if white_player else b.black
    opponents = b.black if white_player else b.white
    # Vi burde nok få den til at undgå uafgjorte kampe.
    return len(players) / len(opponents) if len(opponents) > 0 else 100


def max_node(nodes: list[Node]) -> Node:
    """Return the node with the greatest value."""
    return reduce(lambda mn, n: n if n.value > mn.value else mn, nodes)


def mini_node(nodes: list[Node]) -> Node:
    """Return the node with the smallest value."""
    return reduce(lambda mn, n: n if n.value < mn.value else mn, nodes)
