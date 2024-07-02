"""
Module to define Minesweeper Board controller
"""
from collections import defaultdict
from random import randrange


class Board:
    """
    Board class that configures the logical minesweeper board
    and controls its logic.
    """

    def __init__(self, size: int, number_of_mines: int):
        self.__size: int = size
        self.__number_of_mines: int = number_of_mines
        self.__cells: list[list[str]] = []
        self.__hints: list[list[int]] = []
        self.__adj_map: dict[tuple[int, int], set[tuple[int, int]]] = defaultdict(set)
        self.__mine_positions: set[tuple[int, int]] = set()
        self.__game_ended: bool = False
        self.__has_lost: bool = False
        self.__has_won: bool = False

        self.__init_empty_board()
        self.__place_mines()
        self.__fill_hints()
        self.__fill_adj_map()

    @property
    def size(self) -> int:
        """
        Returns the value of the size property.
            Returns:
                 size (int): an int value indicating the size of the board.
        """
        return int(self.__size)

    @property
    def number_of_mines(self) -> int:
        """
        Returns the value of the number_of_mines property.
            Returns:
                 size (int): an int value indicating the number of mines in the board.
        """
        return int(self.__number_of_mines)

    @property
    def mine_positions(self) -> set[tuple[int, int]]:
        """
        Returns the value of the mine_positions property.
            Returns:
                 size (set[tuple[int, int]]): a set of [col, row] positions indicating the position
                 of the mines in the board.
        """
        return self.__mine_positions.copy()

    @property
    def game_ended(self) -> bool:
        """
        Returns the value of the game_ended property.
            Returns:
                 game_ended (bool): a boolean value indicating whether the game has ended or not.
        """
        return bool(self.__game_ended)

    @property
    def lost(self) -> bool:
        """
        Returns the value of the lost property.
            Returns:
                 lost (bool): a boolean value indicating whether the user lost or not.
        """
        return bool(self.__has_lost)

    @property
    def won(self) -> bool:
        """
        Returns the value of the won property.
            Returns:
                 won (bool): a boolean value indicating whether the user won or not.
        """
        return bool(self.__has_won)

    def __init_empty_board(self):
        self.__cells = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.__hints = [[0 for _ in range(self.size)] for _ in range(self.size)]

    def __place_mines(self) -> None:
        placed_mines: int = 0
        while placed_mines < self.number_of_mines:
            random_row = randrange(0, self.size)
            random_col = randrange(0, self.size)
            if (random_row, random_col) not in self.mine_positions:
                self.__mine_positions.add((random_row, random_col))
                placed_mines += 1

    def __fill_hints(self) -> None:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        for row, _ in enumerate(self.__cells):
            for col, _ in enumerate(self.__cells[row]):
                adjacent_mines: int = 0

                for d in directions:
                    delta_row, delta_col = d[0], d[1]
                    new_row = row + delta_row
                    new_col = col + delta_col
                    if (0 <= new_row < self.size and 0 <= new_col < self.size and
                            (new_row, new_col) in self.__mine_positions):
                        adjacent_mines += 1
                self.__hints[row][col] = adjacent_mines

    def __fill_adj_map(self):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        for row, _ in enumerate(self.__hints):
            for col, _ in enumerate(self.__hints[row]):
                if self.__hints[row][col] == 0 and (row, col) not in self.mine_positions:
                    for d in directions:
                        delta_row, delta_col = d[0], d[1]
                        new_row = row + delta_row
                        new_col = col + delta_col
                        if (0 <= new_row < self.size and 0 <= new_col < self.size and
                                self.__hints[new_row][new_col] == 0):
                            self.__adj_map[(row, col)].add((new_row, new_col))

    def click(self, row: int, col: int) -> bool:
        """
        Simulates a 0-based click event on the board at [row, col].
        """

        # Block clicks if the game ended
        if self.game_ended:
            return False

        # Do nothing if there's a repeated click
        if self.__cells[row][col] != ' ':
            return True

        # User selected a mine
        if (row, col) in self.mine_positions:
            self.__end_game(True)
            return False

        # User selected a cell = 0
        if self.__hints[row][col] == 0:
            origin = (row, col)
            stack = [origin]
            seen = set()

            while stack:
                node = stack.pop()
                if node in seen:
                    continue
                seen.add(node)
                self.__cells[node[0]][node[1]] = '0'
                for neighbor in self.__adj_map[node]:
                    stack.append(neighbor)
            if self.all_cells_clicked():
                self.__end_game(False)

            return True

        # User selected a cell != 0 and not a mine
        self.__cells[row][col] = f'{self.__hints[row][col]}'
        if self.all_cells_clicked():
            self.__end_game(False)
        return True

    def all_cells_clicked(self) -> bool:
        """
        Returns a boolean value indicated if the player has won.
        True if player has won the game.
        """
        empty_cells = 0
        for x in self.__cells:
            for y in x:
                if y == ' ':
                    empty_cells += 1
        if empty_cells == self.number_of_mines:
            return True
        return False

    def __end_game(self, lost: bool):
        self.__reveal_mines()
        self.__game_ended = True
        if lost:
            self.__has_lost, self.__has_won = True, False
        else:
            self.__has_lost, self.__has_won = False, True

    def __reveal_mines(self):
        for (row, col) in self.mine_positions:
            self.__cells[row][col] = 'X'

    def print_visual_board(self):
        """
        Prints a visual representation of the board.
        """
        for x in self.__cells:
            print(f'{x}\n')

    def __repr__(self) -> str:
        printable_board: str = 'Board:\n'

        for cell in self.__cells:
            printable_board += f'{cell}\n'

        printable_board += '\nHints:\n'

        for hint in self.__hints:
            printable_board += f'{hint}\n'

        printable_board += '\nMines:\n'
        printable_board += f'{self.mine_positions}\n'

        return printable_board
