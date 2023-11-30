from board import *
from minimax import *


def input_bool(prompt: str) -> bool:
    """Ask the user a question using prompt. Accept yes, y, no or n as answers.
    If the answer is invalid, ask the user again.
    """
    answer = input(prompt + "\n")
    while answer not in ["yes", "y", "no", "n"]:
        answer = input("Please enter yes or no.\n")
    return answer in ["yes", "y"]


def input_int(minimum: int, maximum: int, prompt: str) -> int:
    """Ask the user for a number using prompt.
    Accept only numbers between minimum and maximum both inclusive.
    If the number is invalid, ask the user again.
    """
    number = int(input(prompt + "\n"))
    while not minimum <= number <= maximum:
        number = int(input(f"Please enter a number between"
                           f"{minimum} and {maximum}.\n"))
    return number


def input_move(b: Board) -> Move:
    """Ask the user for a legal move. Keep prompting until one is gotten."""
    has_found_legal_move = False
    while not has_found_legal_move:
        src = input_int(1, 25, "What piece do you want to move?")
        trg = input_int(1, 25, "Where should the piece go?")
        player_move = make_move(src, trg)
        if is_legal(player_move, b):
            has_found_legal_move = True
        else:
            print("That isn't possible. Here are the legal moves:")
            print_moves(b)
    return player_move


def print_board(b: Board, dark_mode: bool) -> None:
    """Print a board in the terminal."""
    black_dot = "○" if dark_mode else "●"
    white_dot = "●" if dark_mode else "○"
    v = [black_dot if i in black(b) else
         white_dot if i in white(b) else
         " "
         for i in range(1, 26)]

    print(f"{v[0]} - {v[1]} - {v[2]} - {v[3]} - {v[4]}",
          "| \ | / | \ | / |",
          f"{v[5]} - {v[6]} - {v[7]} - {v[8]} - {v[9]}",
          "| / | \ | / | \ |",
          f"{v[10]} - {v[11]} - {v[12]} - {v[13]} - {v[14]}",
          "| \ | / | \ | / |",
          f"{v[15]} - {v[16]} - {v[17]} - {v[18]} - {v[19]}",
          "| / | \ | / | \ |",
          f"{v[20]} - {v[21]} - {v[22]} - {v[23]} - {v[24]}", 
          sep="\n")


def print_moves(b: Board) -> None:
    """Print a list of the legal moves for a given board."""
    for legal_move in legal_moves(b):
        print(f"{source(legal_move)} to {target(legal_move)}", end=", ")
    print()


def play_alquerque():
    """Play a game of alquerque."""
    print("\nIt's time to get quirky, let's play some Alquerque!\n")

    print("Before we start:\n")

    dark_mode = input_bool("Are you using dark mode? (yes/no)")
    white_is_ai = input_bool("Should the computer play white? (yes/no)")
    black_is_ai = input_bool("Should the computer play black? (yes/no)")
    if white_is_ai or black_is_ai:
        ai_difficulty = input_int(
            1, 7,
            "How hard should the computer be? (1-7)")

    print("This is the game board with it's indices.\n")

    print("1  - 2  - 3  - 4  - 5")
    print("|  \ |  / |  \ |  / |")
    print("6  - 7  - 8  - 9  - 10")
    print("|  / |  \ |  / |  \ |")
    print("11 - 12 - 13 - 14 - 15")
    print("|  \ |  / |  \ |  / |")
    print("16 - 17 - 18 - 19 - 20")
    print("|  / |  \ |  / |  \ |")
    print("21 - 22 - 23 - 24 - 25\n")

    print("Ready, set, go!\n")

    b = make_board()

    while not is_game_over(b):
        print_board(b, dark_mode)
        color = "white" if white_plays(b) else "black"
        if (white_plays(b) and white_is_ai
                or not white_plays(b) and black_is_ai):
            ai_move = next_move(b, ai_difficulty)
            move(ai_move, b)
            print(f"The computer moved a {color} piece from "
                  f"{source(ai_move)} to {target(ai_move)}")
        else:
            print(f"Make a move for {color}.")
            player_move = input_move(b, dark_mode)
            move(player_move, b)
        print()

    print_board(b, dark_mode)
    print("    Game over\n")

    if not white(b):
        print("Black has won!")
    elif not black(b):
        print("White has won!")
    else:
        print("It's a draw!")
    print()


play_alquerque()
