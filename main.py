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

from typing import Any

from board import Board
from validator import Validator
from constants import Constants


def main() -> None:
    """
    Main logic for game controller.
    """
    is_valid_input: bool = False
    board_size: Any = None
    number_of_mines: Any = None
    while not is_valid_input:
        board_size = input("Size of board?\n")
        number_of_mines = input("Number of mines?\n")

        conf_errors = Validator.get_configuration_errors(board_size, number_of_mines)
        if not conf_errors:
            is_valid_input = True
        else:
            print(conf_errors)

    board_size_int: int = int(board_size)
    number_of_mines_int: int = int(number_of_mines)
    board = Board(board_size_int, number_of_mines_int)
    print(board)

    click_number = 1
    while not board.game_ended:
        row_selection = input(f"Select a row between [0-{board_size_int - 1}]\n")
        col_selection = input(f"Select a col between [0-{board_size_int - 1}]\n")
        if not Validator.is_in_range(
            row_selection, board_size_int
        ) or not Validator.is_in_range(col_selection, board_size_int):
            print("Row or Col are invalid")
            continue

        row_selection_int = int(row_selection)
        col_selection_int = int(col_selection)
        print(f"Click {click_number}: ({row_selection_int}, {col_selection_int})")
        board.click(row_selection_int, col_selection_int)
        board.print_visual_board()
        click_number += 1

    print(f"\n\n{Constants.blue()}End of the Game{Constants.color_off()}")
    print(board)
    if board.lost:
        print(f"{Constants.red()}You lost !{Constants.color_off()}")
    if board.won:
        print(f"{Constants.green()}You won !{Constants.color_off()}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(
            f"{Constants.reset()}{Constants.red()}"
            f"User interrupted execution.{Constants.color_off()}"
        )
