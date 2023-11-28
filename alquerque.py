from board import *
from minimax import *


def ask_yes_or_no(prompt: str) -> bool:
    """Ask the user a question using prompt. Accept yes, y, no or n as answers.
    If the answer is invalid, ask the user again using repeat_prompt.
    """
    answer = input(prompt + '\n')
    while answer not in ['yes', 'y', 'no', 'n']:
        answer = input("Enter yes or no.\n")
    return answer in ['yes', 'y']


def ask_for_number(minimum: int, maximum: int, prompt: str) -> int:
    """Ask the user for a number using prompt.
    Accept only numbers between minimum and maximum both inclusive.
    If the number is invalid, ask the user again using repeat_prompt.
    """
    number = int(input(prompt + '\n'))
    while number < minimum or maximum < number:
        number = int(input(f"Enter a number between {minimum} and {maximum}."))
    return number


def ask_for_move(b: Board) -> Move:
    """Ask the user for a legal move. Keep prompting until one is gotten."""
    has_found_legal_move = False
    while not has_found_legal_move:
        source = ask_for_number(1, 25, "What piece do you want to move?")
        target = ask_for_number(1, 25, "Where should the piece go?")
        next_move = make_move(source, target)
        if is_legal(next_move, b):
            has_found_legal_move = True
        else:
            print("That isn't possible. Here are the legal moves:")
            print_moves(b)
    return next_move


def print_board(b: Board) -> None:
    v = []
    black_dot = "○" if dark_mode else "●"
    white_dot = "●" if dark_mode else "○"
    for index in range(1, 26):
        if index in black(b):
            v.append(black_dot)
        elif index in white(b):
            v.append(white_dot)
        else:
            v.append(" ")

    print(f"{v[0]} - {v[1]} - {v[2]} - {v[3]} - {v[4]}")
    print(f"| \ | / | \ | / |")
    print(f"{v[5]} - {v[6]} - {v[7]} - {v[8]} - {v[9]}")
    print(f"| / | \ | / | \ |")
    print(f"{v[10]} - {v[11]} - {v[12]} - {v[13]} - {v[14]}")
    print(f"| \ | / | \ | / |")
    print(f"{v[15]} - {v[16]} - {v[17]} - {v[18]} - {v[19]}")
    print(f"| / | \ | / | \ |")
    print(f"{v[20]} - {v[21]} - {v[22]} - {v[23]} - {v[24]}")


def print_moves(b: Board) -> None:
    for move in legal_moves(b):
        print(f"{source(move)} to {target(move)}", end=", ")
    print()


print("\nIt's time to get quirky, let's play some Alquerque!\n")

print("Before we start:\n")

dark_mode = ask_yes_or_no("Are you using dark mode? (yes/no)")
white_is_ai = ask_yes_or_no("Should the computer play white? (yes/no)")
black_is_ai = ask_yes_or_no("Should the computer play black? (yes/no)")
if white_is_ai or black_is_ai:
    ai_difficulty = ask_for_number(
        1, 7,
        "How hard should the computer be? (1-7)")

print("This is the board with it's indices.\n")

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
    print_board(b)
    color = "white" if white_plays(b) else "black"
    if white_plays(b) and white_is_ai or not white_plays(b) and black_is_ai:
        ai_move = next_move(b, ai_difficulty)
        move(ai_move, b)
        print(f"The computer moved a {color} piece from",
              f"{source(ai_move)} to {target(ai_move)}\n")
    else:
        print(f"Make a move for {color}.")
        move(ask_for_move(b), b)
        print()


print_board(b)
print("    Game over\n")

if not white(b):
    print("Black has won!")
elif not black(b):
    print("White has won!")
else:
    print("It's a draw!")
