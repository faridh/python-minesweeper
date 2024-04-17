"""
Write a minesweeper program, expect you will receive the input in the command line
Assume a matrix of NxN
The output of the program is the minesweeper board
The input you will receive is the X,Y coordinates you want to uncover
The program runs until either the person hits a mine or they finish uncovering all the non-mine pieces

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

Assume the player can input the N for the size of the board, and also the number of mines? up to you 
"""

from random import randrange

from board.board import Board
from validator.validator import Validator

if __name__ == '__main__':
    valid_input = False
    while not valid_input:
        board_size = input('Size of board?\n')
        number_of_mines = input('Number of mines?\n')

        conf_errors = Validator.get_configuration_errors(board_size, number_of_mines)
        if not conf_errors:
            valid_input = True
        else:
            print(conf_errors)

    board_size = int(board_size)
    number_of_mines = int(number_of_mines)
    board = Board(board_size, number_of_mines)
    print(board)

    click_number = 1
    while not board.game_ended:
        row_selection = input(f'Select a row between [0-{board_size-1}]\n')
        col_selection = input(f'Select a col between [0-{board_size-1}]\n')
        if (not Validator.is_in_range(row_selection, board_size)
                or not Validator.is_in_range(col_selection, board_size)):
            print(f'Row or Col are invalid')
            continue

        row_selection = int(row_selection)
        col_selection = int(col_selection)
        print(f'Click {click_number}: ({row_selection}, {col_selection})')
        board.click(row_selection, col_selection)
        board.print_visual_board()
        click_number += 1

    print('\n\nEnd of the Game')
    print(board)

