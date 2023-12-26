from os import getcwd
import tkinter as tk
from tkinter import messagebox, simpledialog
from functools import partial
from board import *
from minimax import next_move
from minimax_v2 import next_move as next_move_v2
import time

def init_squares() -> list[tk.Button]:
    """Initialize the list of squares."""
    squares = [None] # dummy
    for i in range(5):
        for j in range(5):
            b = make_button(2*i,2*j,i*5+j+1)
            squares.append(b)
            # separator
            if j < 4:
                make_separator(2*i,2*j+1,img_H)
        # separators
        for j in range(5):
            if i < 4:
                make_separator(2*i+1,2*j,img_V)
                if j<4 and i%2 == j%2:
                    make_separator(2*i+1,2*j+1,img_D)
                elif j<4:
                    make_separator(2*i+1,2*j+1,img_U)
    return squares

def get_params() -> None:
    """Let the user configure the game."""
    global white_AI, black_AI, AI_level
    messagebox.showinfo('Hello!',
                        "Welcome to Alquerque!")
    white_AI = messagebox.askyesno('Before we start...',
                                   "Should the computer play white?")
    black_AI = messagebox.askyesno('Before we start...',
                                   "Should the computer play black?")
    if white_AI or black_AI:
        AI_level = 0
        while not 1 <= AI_level <= 7:
            AI_level = simpledialog.askinteger('Before we start...',
                                               "How smart should the computer be (1-7)?")
            if not 1 <= AI_level <= 7:
                messagebox.showerror('Before we start...',
                                     'Please enter a number in the range 1-7.')
    messagebox.showwarning('Ready!',
                           "The game will now start!")

def make_button(i: int, j: int, label: int) -> tk.Button:
    """Creates a standard square button."""
    frame = tk.Frame(master=root)
    frame.grid(row=i,column=j)
    button = tk.Button(master=frame,
                       text=label,
                       image=img_empty)
    button.pack()
    return(button)

def make_separator(i: int, j: int, img: tk.PhotoImage) -> tk.Button:
    """Creates a separator button."""
    frame = tk.Frame(master=root)
    frame.grid(row=i,column=j)
    tk.Label(master=frame,
             image=img,
             fg="white").pack()

def redraw() -> None:
    """Redraws the board."""
    for i in range(1,26):
        squares[i]['image'] = img_empty
    for i in white(board):
        squares[i]['image'] = img_white
    for i in black(board):
        squares[i]['image'] = img_black

def activate_sources() -> None:
    """Activates all pieces that can be moved."""
    for m in legal_moves(board):
        i,j = (source(m),target(m))
        squares[i].bind("<Button-1>",partial(move_me, src=i))

def activate_targets(src: int) -> None:
    """Activates all slots to which the selected piece can be moved."""
    for m in legal_moves(board):
        i,j = (source(m),target(m))
        if src == i:
            squares[j].bind("<Button-1>",partial(move_here, src=i, tgt=j))

def deactivate_all() -> None:
    """Removes all events."""
    for i in range(1,26):
        squares[i].unbind("<Button-1>")

def move_me(event, src: int) -> None:
    """Selects a piece to move and activates corresponding events."""
    button = event.widget
    button['image'] = img_white_sel if white_plays(board) else img_black_sel
    deactivate_all()
    button.bind("<Button-1>",regret)
    activate_targets(src)

def regret(event) -> None:
    """If the player unselects the piece."""
    button = event.widget
    button['image'] = img_white if white_plays(board) else img_black
    activate_sources()

def move_here(event, src: int, tgt: int) -> None:
    """Performs a move."""
    move(make_move(src,tgt),board)
    relax()

def move_AI() -> None:
    """Makes a computer move."""
    deactivate_all()
    time.sleep(1)
    if white_plays(board):
        move(next_move_v2(board,AI_level),board)
    else:
        move(next_move(board,AI_level),board)
    relax()

def relax() -> None:
    """Get ready for the next move."""
    redraw()
    deactivate_all()
    root.update()
    root.update_idletasks()
    if is_game_over(board):
        cleanup()
    elif white_plays(board) and white_AI:
        move_AI()
    elif not white_plays(board) and black_AI:
        move_AI()
    else:
        redraw()
        activate_sources()

def cleanup() -> None:
    """Game over!"""
    root.destroy()
    if white_plays(board) and white(board) == []:
        messagebox.showinfo('Game over!','Black has won!')
    elif not white_plays(board) and black(board) == []:
        messagebox.showinfo('Game over!','White has won!')
    else:
        messagebox.showinfo('Game over!','The game is a draw...')
    
get_params()
root = tk.Tk()
# images - seriously?!
img_black = tk.PhotoImage(file=getcwd()+"/img/black.png")
img_black_sel = tk.PhotoImage(file=getcwd()+"/img/blackSel.png")
img_white = tk.PhotoImage(file=getcwd()+"/img/white.png")
img_white_sel = tk.PhotoImage(file=getcwd()+"/img/whiteSel.png")
img_empty = tk.PhotoImage(file=getcwd()+"/img/empty.png")
img_D = tk.PhotoImage(file=getcwd()+"/img/D.png")
img_H = tk.PhotoImage(file=getcwd()+"/img/H.png")
img_U = tk.PhotoImage(file=getcwd()+"/img/U.png")
img_V = tk.PhotoImage(file=getcwd()+"/img/V.png")

squares = init_squares()
board = make_board()
relax()
root.mainloop()

