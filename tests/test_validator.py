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
    def test_validates_board_size_successfully(self) -> None:
        result: list[ValidationError] = Validator.get_configuration_errors('3', '1')
        self.assertEqual(len(result), 1)
        self.assertEqual(type(result[0]), BoardSizeError)

        result: list[ValidationError] = Validator.get_configuration_errors('21', '1')
        self.assertEqual(len(result), 1)
        self.assertEqual(type(result[0]), BoardSizeError)

        result: list[ValidationError] = Validator.get_configuration_errors('a', '1')
        self.assertEqual(len(result), 1)
        self.assertEqual(type(result[0]), BoardSizeError)

    def test_validates_number_of_mines_successfully(self) -> None:
        result: list[ValidationError] = Validator.get_configuration_errors('5', '1')
        self.assertEqual(len(result), 1)
        self.assertEqual(type(result[0]), NumberOfMinesError)

        result: list[ValidationError] = Validator.get_configuration_errors('5', '7')
        self.assertEqual(len(result), 1)
        self.assertEqual(type(result[0]), NumberOfMinesError)

        result: list[ValidationError] = Validator.get_configuration_errors('5', 'a')
        self.assertEqual(len(result), 1)
        self.assertEqual(type(result[0]), NumberOfMinesError)

    def test_validates_configuration_successfully(self) -> None:
        result: list[ValidationError] = Validator.get_configuration_errors('4', '2')
        self.assertEqual(len(result), 0)

        result: list[ValidationError] = Validator.get_configuration_errors('4', '4')
        self.assertEqual(len(result), 0)

        result: list[ValidationError] = Validator.get_configuration_errors('10', '5')
        self.assertEqual(len(result), 0)

        result: list[ValidationError] = Validator.get_configuration_errors('10', '25')
        self.assertEqual(len(result), 0)
