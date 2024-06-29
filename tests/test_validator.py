"""
UTs fot Validator
"""
import unittest

from errors import BoardSizeError, NumberOfMinesError, ValidationError
from validator import Validator


class TestValidator(unittest.TestCase):
    """
    Defines unit tests for Validator class
    """

    def test_should_validate_board_size_successfully(self) -> None:
        """
        Tests that Validator validates the board size successfully
        """
        result: list[ValidationError] = Validator.get_configuration_errors('3', '1')
        self.assertEqual(len(result), 1)
        self.assertEqual(type(result[0]), BoardSizeError)

        result: list[ValidationError] = Validator.get_configuration_errors('21', '1')
        self.assertEqual(len(result), 1)
        self.assertEqual(type(result[0]), BoardSizeError)

        result: list[ValidationError] = Validator.get_configuration_errors('a', '1')
        self.assertEqual(len(result), 1)
        self.assertEqual(type(result[0]), BoardSizeError)

    def test_should_validate_number_of_mines_successfully(self) -> None:
        """
        Tests that Validator validates the number of mines successfully
        """
        result: list[ValidationError] = Validator.get_configuration_errors('5', '1')
        self.assertEqual(len(result), 1)
        self.assertEqual(type(result[0]), NumberOfMinesError)

        result: list[ValidationError] = Validator.get_configuration_errors('5', '7')
        self.assertEqual(len(result), 1)
        self.assertEqual(type(result[0]), NumberOfMinesError)

        result: list[ValidationError] = Validator.get_configuration_errors('5', 'a')
        self.assertEqual(len(result), 1)
        self.assertEqual(type(result[0]), NumberOfMinesError)

    def test_should_validate_configuration_successfully(self) -> None:
        """
        Tests that Validator validates a valid configuration successfully
        """
        for board_size in range(4, 21):
            min_mines = board_size // 2
            max_mines = board_size ** 2 // 4
            for num_mines in range(min_mines, max_mines + 1):
                result: list[ValidationError] = (
                    Validator.get_configuration_errors(str(board_size), str(num_mines)))
                self.assertEqual(len(result), 0)
