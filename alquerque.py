# Hello! Welcome to Alquerque!
# Before we start...
    # Should the computer play white (y/n)?
        # Please answer y or n.
    # Should the computer play black (y/n)?
        # Please answer y or n.
    # How smart should the computer be (1-7)?
        # Please enter a number in the range 1-7.
# Ready!
    # The game will now start!
# Game over!
    # Black has won!
    # White has won!
    # The game is a draw...


def ask_yes_or_no(prompt: str, repeat_prompt: str) -> bool:
    """Ask the user a question using prompt. Accept yes, y, no or n as answers.
    If the answer is invalid, ask the user again using repeat_prompt.
    """
    answer = input(prompt)
    while answer not in ['yes', 'y', 'no', 'n']:
        answer = input(repeat_prompt)
    return answer in ['yes', 'y']


def ask_for_number(prompt: str, repeat_prompt: str,
                   minimum: int, maximum: int) -> int:
    """Ask the user for a number using prompt.
    Accept only numbers between minimum and maximum both inclusive.
    If the number is invalid, ask the user again using repeat_prompt.
    """
    number = int(input(prompt))
    while number < minimum or maximum < number:
        number = int(input(repeat_prompt))
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


print("""
It's time to get quirky, let's play some Alquerque!

You can hear the crowd cheer, but first let's get the rules clear...

Will you stand in the limelight or will you let the AI be white? (y/n)
    Please just type y or n, it's all that we need.
    You know who'd be proud of you? Frances Shand Kydd.

If you need to hit the sack, will you just let the AI play black? (y/n)
    I really am feeling the rhythm and blues,
    a simple y or n, that's all you have to choose.

We crafted this software, it's a true piece of art,
now decide, should the AI be dumb or smart? (1-7)
    With that attitude you won't come into heaven,
    so please just pick a number between 1 and 7.

It's time to get started, find your laminar flow. Let's hope your hands are steady. Ready, set, go!

You fought with all your might and the game is now done,
so it's a pleasure to announce that ... won!

This game was as complex as the United States national law,
but in the end 'twas for nothing, it ended in a draw.
""")

