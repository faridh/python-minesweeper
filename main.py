"""
Write a minesweeper program, expect you will receive the input in the command
line.
Assume a matrix of NxN
The output of the program is the minesweeper board
The input you will receive is the X,Y coordinates you want to uncover
The program runs until either the person hits a mine or they finish uncovering
all the non-mine pieces.

Board:
X X X X
X X X X
X X X X
X X X X

X X X X
X 2 X X
X X X X
X X X X

X X X X
1 2 X X
X X X X
X X X X

Assume the player can input the N for the size of the board, and also the
number of mines? Up to you.
"""

from board.board import Board
from validator.validator import Validator

if __name__ == '__main__':
    VALID_INPUT = False
    while not VALID_INPUT:
        board_size = input('Size of board?\n')
        number_of_mines = input('Number of mines?\n')

        conf_errors = Validator.get_configuration_errors(board_size, number_of_mines)
        if not conf_errors:
            VALID_INPUT = True
        else:
            print(conf_errors)

    board_size_int = int(board_size)
    number_of_mines_int = int(number_of_mines)
    board = Board(board_size_int, number_of_mines_int)
    print(board)

    CLICK_NUMBER = 1
    while not board.game_ended:
        row_selection = input(f'Select a row between [0-{board_size_int-1}]\n')
        col_selection = input(f'Select a col between [0-{board_size_int-1}]\n')
        if (not Validator.is_in_range(row_selection, board_size_int)
                or not Validator.is_in_range(col_selection, board_size_int)):
            print('Row or Col are invalid')
            continue

        row_selection_int = int(row_selection)
        col_selection_int = int(col_selection)
        print(f'Click {CLICK_NUMBER}: ({row_selection_int}, {col_selection_int})')
        board.click(row_selection_int, col_selection_int)
        board.print_visual_board()
        CLICK_NUMBER += 1

    print('\n\nEnd of the Game')
    print(board)
