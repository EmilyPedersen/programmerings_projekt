from board import *
from minimax import *


def ask_yes_or_no(prompt: str, repeat_prompt: str) -> bool:
    """Ask the user a question using prompt. Accept yes, y, no or n as answers.
    If the answer is invalid, ask the user again using repeat_prompt.
    """
    answer = input(prompt + '\n')
    while answer not in ['yes', 'y', 'no', 'n']:
        answer = input(repeat_prompt + '\n')
    return answer in ['yes', 'y']


def ask_for_number(minimum: int, maximum: int,
                   prompt: str, repeat_prompt: str) -> int:
    """Ask the user for a number using prompt.
    Accept only numbers between minimum and maximum both inclusive.
    If the number is invalid, ask the user again using repeat_prompt.
    """
    number = int(input(prompt + '\n'))
    while number < minimum or maximum < number:
        number = int(input(repeat_prompt + '\n'))
    return number


def ask_for_move(b: Board) -> Move:
    """Ask the user for a legal move. Keep prompting until one is gotten."""
    print("Get in the groove, it's time for you to make a move!")
    has_found_legal_move = False
    while not has_found_legal_move:
        source = ask_for_number(
            1, 25, "Which piece do you want to move?", "???")
        target = ask_for_number(
            1, 25, "Where do you want to move your piece?", "???")
        next_move = make_move(source, target)
        if is_legal(next_move, b):
            has_found_legal_move = True
        else:
            print("That's not quite possible, we might have an issue. If you want to make it right, here are some moves you can do:")
            print_moves(b)
    return next_move


def print_board(b: Board) -> None:
    v = []
    for index in range(1, 26):
        if index in black(b):
            v.append("●")
        elif index in white(b):
            v.append("○")
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

print("You can hear the crowd cheer, but first let's get the rules clear...\n")

white_is_ai = ask_yes_or_no(
    "Will you step away from the limelight and let the AI play white? (yes/no)",
    "Please just type yes or no, it's all that we need. You know who'd be proud of you? Frances Shand Kydd.")
black_is_ai = ask_yes_or_no(
    "It look like you need to hit the sack, will you just let the AI play black? (yes/no)",
    "I'm really feeling the rhythm of the blues, a simple yes or no, that's all you have to choose.")
ai_difficulty = ask_for_number(
    1, 7,
    "We crafted this software, it's a true piece of art, now you must decide, should the AI be dumb or smart? (1-7)",
    "With an attitude like that you won't get into heaven, so please just pick a number between 1 and 7.")

print("This is the board we'll be playing on tonight. Get to know it now, so you don't end up losing sight.\n")

print("01 - 02 - 03 - 04 - 05")
print("|  \ |  / |  \ |  / |")
print("06 - 07 - 08 - 09 - 10")
print("|  / |  \ |  / |  \ |")
print("11 - 12 - 13 - 14 - 15")
print("|  \ |  / |  \ |  / |")
print("16 - 17 - 18 - 19 - 20")
print("|  / |  \ |  / |  \ |")
print("21 - 22 - 23 - 24 - 25\n")

print("It's time to get started, so find your laminar flow. Let's hope your hands are steady. Ready, set, go!\n")

b = make_board()

while not is_game_over(b):
    print_board(b)

    if white_plays(b):
        print("  White's turn\n")
    else:
        print("  Black's turn\n")

    if white_plays(b) and white_is_ai or not white_plays(b) and black_is_ai:
        ai_move = next_move(b, ai_difficulty)
        move(ai_move, b)
        print(f"The computer moved from {source(ai_move)} to {target(ai_move)}\n")
    else:
        move(ask_for_move(b), b)
        print()


print_board(b)
print("    Game over\n")

if not white(b):
    print("You fought with all your might and the game is now done, so it's a pleasure to announce that black won!")
elif not black(b):
    print("You fought with all your might and the game is now done, so it's a pleasure to announce that white won!")
else:
    print("This game was as complex as the U.S. nationality law, but in the end 'twas for nothing... it ended in a draw.")
