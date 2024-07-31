"""
Validator module
"""

from errors import BoardSizeError, NumberOfMinesError, ValidationError


class Validator:
    """
    Validates the configuration of the Board.
    """

    min_board_size = 4
    max_board_size = 20

    @staticmethod
    def get_configuration_errors(
        board_size: str, number_of_mines: str
    ) -> list[ValidationError]:
        """
        Returns a list of ValidationError if existent.
        Returns an empty list if there are no ValidationErrors.
        """
        errors: list[ValidationError] = []
        if not Validator.__valid_board_size(board_size):
            errors.append(
                BoardSizeError(Validator.min_board_size, Validator.max_board_size)
            )
            return errors

        b_size = int(board_size)
        if not Validator.__valid_number_of_mines(b_size, number_of_mines):
            min_mines = Validator.__min_valid_mines(b_size)
            max_mines = Validator.__max_valid_mines(b_size)
            errors.append(NumberOfMinesError(min_mines, max_mines))
        return errors

    @staticmethod
    def __valid_board_size(board_size: str) -> bool:
        if not Validator.__is_integer(board_size):
            return False

        b_size = int(board_size)
        if not Validator.min_board_size <= b_size <= Validator.max_board_size:
            return False
        return True

    @staticmethod
    def __valid_number_of_mines(board_size: int, number_of_mines: str) -> bool:
        board_size = int(board_size)
        if not Validator.__is_integer(number_of_mines):
            return False

        n_of_mines = int(number_of_mines)
        min_mines = Validator.__min_valid_mines(board_size)
        max_mines = Validator.__max_valid_mines(board_size)
        if not min_mines <= n_of_mines <= max_mines:
            return False

        return True

    @staticmethod
    def __is_integer(input_str: str) -> bool:
        try:
            _ = int(input_str)
        except ValueError:
            return False
        return True

    @staticmethod
    def is_in_range(value: str, size: int) -> bool:
        """
        Determines if a value is in the [0, size) range.
        """
        if not Validator.__is_integer(value):
            return False
        v = int(value)
        if v not in range(0, size):
            return False
        return True

    @staticmethod
    def __min_valid_mines(board_size: int) -> int:
        return board_size // 2

    @staticmethod
    def __max_valid_mines(board_size: int) -> int:
        return board_size**2 // 4  # ~25 % total cells
