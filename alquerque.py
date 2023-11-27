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


def print_board(b: Board):
    v = []
    for index in range(1, 26):
        if index in black(b):
            v += ["●"]
        elif index in white(b):
            v += ["○"]
        else:
            v += [" "]

    print(f"""
{v[0]} - {v[1]} - {v[2]} - {v[3]} - {v[4]}
| \ | / | \ | / |
{v[5]} - {v[6]} - {v[7]} - {v[8]} - {v[9]}
| / | \ | / | \ |
{v[10]} - {v[11]} - {v[12]} - {v[13]} - {v[14]}
| \ | / | \ | / |
{v[15]} - {v[16]} - {v[17]} - {v[18]} - {v[19]}
| / | \ | / | \ |
{v[20]} - {v[21]} - {v[22]} - {v[23]} - {v[24]}""")


print("\nIt's time to get quirky, let's play some Alquerque!\n")

print("You can hear the crowd cheer, but first let's get the rules clear...\n")

white_is_ai = ask_yes_or_no(
    "Will you stand in the limelight or will you let the AI be white? (y/n)",
    "Please just type y or n, it's all that we need. You know who'd be proud of you? Frances Shand Kydd.")
black_is_ai = ask_yes_or_no(
    "If you need to hit the sack, will you just let the AI play black? (y/n)",
    "I really am feeling the rhythm and blues, a simple y or n, that's all you have to choose.")
ai_difficulty = ask_for_number(
    1, 7,
    "We crafted this software, it's a true piece of art, now decide, should the AI be dumb or smart? (1-7)",
    "With that attitude you won't come into heaven, so please just pick a number between 1 and 7.")

print("This is the board we'll be playing tonight. Get to know it now, so you don't lose sight.\n")

print("""01 - 02 - 03 - 04 - 05
|  \ |  / |  \ |  / |
06 - 07 - 08 - 09 - 10
|  / |  \ |  / |  \ |
11 - 12 - 13 - 14 - 15
|  \ |  / |  \ |  / |
16 - 17 - 18 - 19 - 20
|  / |  \ |  / |  \ |
21 - 22 - 23 - 24 - 25
""")

print("It's time to get started, find your laminar flow. Let's hope your hands are steady. Ready, set, go!\n")

b = make_board()

while not is_game_over(b):
    print_board(b)

    if white_plays(b):
        print("White's turn")
    else:
        print("Black's turn")

    if white_plays(b) and white_is_ai or not white_plays(b) and black_is_ai:
        move(next_move(b, ai_difficulty), b)
    else:
        source = ask_for_number(
            1, 25, "Which piece do you want to move?", "???")
        target = ask_for_number(
            1, 25, "Where do you want to move your piece?", "???")
        current_move = make_move(source, target)
        if is_legal(current_move, b):
            move(current_move, b)
        else:
            print("That's not quite possible, we might have an issue. If you want to make it right, here are some moves you can do.")
            print(legal_moves(b))

if not white(b):
    print("You fought with all your might and the game is now done, so it's a pleasure to announce that black won!")
elif not black(b):
    print("You fought with all your might and the game is now done, so it's a pleasure to announce that white won!")
else:
    print("This game was as complex as the United States national law, but in the end 'twas for nothing, it ended in a draw.")
