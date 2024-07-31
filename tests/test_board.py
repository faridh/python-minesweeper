"""
UTs fot Board
"""

import itertools
import unittest

from board import Board


class TestBoard(unittest.TestCase):
    """
    Defines unit tests for Board class
    """

    def test_board_should_init_successfully(self) -> None:
        """
        Tests that the Board is initialized successfully
        """
        subject: Board = Board(5, 2)
        self.assertEqual(subject.size, 5)
        self.assertEqual(subject.number_of_mines, 2)
        self.assertEqual(len(subject.mine_positions), 2)
        self.assertFalse(subject.game_ended)
        self.assertFalse(subject.lost)
        self.assertFalse(subject.won)

    def test_board_should_lose_successfully(self) -> None:
        """
        Tests that the Board ends when a mine is clicked.
        """
        subject: Board = Board(5, 2)
        self.assertFalse(subject.game_ended)
        self.assertFalse(subject.lost)
        mines: set[tuple[int, int]] = subject.mine_positions
        row, col = mines.pop()
        subject.click(row, col)
        self.assertTrue(subject.game_ended)
        self.assertTrue(subject.lost)

    def test_board_should_win_successfully(self) -> None:
        """
        Tests that the Board ends when user clears all mines.
        """
        board_size: int = 5
        subject: Board = Board(board_size, 2)
        self.assertFalse(subject.game_ended)
        self.assertFalse(subject.won)
        rows, cols = list(range(board_size)), list(range(board_size))
        clicks: list[list[int, int]] = itertools.product(rows, cols)
        mines: set[tuple[int, int]] = subject.mine_positions
        for row, col in clicks:
            if (row, col) not in mines:
                subject.click(row, col)
        self.assertTrue(subject.game_ended)
        self.assertTrue(subject.won)
