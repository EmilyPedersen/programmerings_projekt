from board import *
from minimax import *


def input_bool(prompt: str) -> bool:
    """Ask the user a question using prompt.
    Accept yes, y, no or n as answers.
    If the answer is invalid, ask the user again.
    """
    answer = input(f"{prompt} (y/n)\n")
    while answer not in ["yes", "y", "no", "n"]:
        answer = input("Enter yes or no.\n")
    return answer in ["yes", "y"]


def input_int(minimum: int, maximum: int, prompt: str) -> int:
    """Ask the user for a number using prompt.
    Accept only numbers between minimum and maximum both inclusive.
    If the number is invalid, ask the user again.
    """
    number = int(input(f"{prompt} ({minimum}-{maximum})\n"))
    while not minimum <= number <= maximum:
        number = int(input(f"Enter a number from {minimum} to {maximum}.\n"))
    return number


def input_move(b: Board) -> Move:
    """Ask the user for a legal move. Keep prompting until one is gotten."""
    found_legal_move = False
    while not found_legal_move:
        src = input_int(1, 25, "What piece do you want to move?")
        trg = input_int(1, 25, "Where should the piece go?")
        user_move = make_move(src, trg)
        found_legal_move = is_legal(user_move, b)
        if not found_legal_move:
            print("That isn't possible. Here are the legal moves:")
            print_legal_moves(b)
    return user_move


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


def print_legal_moves(b: Board) -> None:
    """Print a list of the legal moves for a given board."""
    for m in legal_moves(b):
        print(f"{source(m)} to {target(m)}, ", end="")
    print()


def play_alquerque():
    """Play a game of alquerque."""
    print("\nIt's time to get quirky, let's play some Alquerque!\n")

    print("Before we start:\n")

    dark_mode = input_bool("Are you using dark mode?")
    ai_white = input_bool("Should the computer play white?")
    ai_black = input_bool("Should the computer play black?")
    if ai_white or ai_black:
        ai_difficulty = input_int(1, 7, "How hard should the computer be?")

    print("\nThis is the game board with it's indices.",
          "These will be used when moving.\n")

    print("1  - 2  - 3  - 4  - 5",
          "|  \ |  / |  \ |  / |",
          "6  - 7  - 8  - 9  - 10",
          "|  / |  \ |  / |  \ |",
          "11 - 12 - 13 - 14 - 15",
          "|  \ |  / |  \ |  / |",
          "16 - 17 - 18 - 19 - 20",
          "|  / |  \ |  / |  \ |",
          "21 - 22 - 23 - 24 - 25",
          sep="\n")

    print("\nTo quit the game simply enter 'q' (or any non number)",
          "and the program will quit (crash).")

    print("\nReady, set, go!\n")

    b = make_board()

    while not is_game_over(b):
        print_board(b, dark_mode)
        print()
        player_color = "white" if white_plays(b) else "black"
        if white_plays(b) and ai_white or not white_plays(b) and ai_black:
            player_move = next_move(b, ai_difficulty)
            print(f"The computer moved a {player_color} piece from "
                  f"{source(player_move)} to {target(player_move)}")
        else:
            print(f"Make a move for {player_color}.")
            player_move = input_move(b)
        move(player_move, b)

    print_board(b, dark_mode)
    print("    Game over\n")

    if white(b) == []:
        print("Black has won!")
    elif black(b) == []:
        print("White has won!")
    else:
        print("It's a draw!")
    print()


play_alquerque()
