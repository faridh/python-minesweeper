"""
Sample documentation for module.
"""
from errors.validationerror import ValidationError


class NumberOfMinesError(ValidationError):
    """
    Represents a configuration error whenever our number of mines is out of
    boundaries.
    """

    message: str

    def __init__(self, min_mines, max_mines):
        self.message = (f'Number of mines should be an integer '
                        f'between {min_mines} and {max_mines} inclusive.')

    def __repr__(self):
        return self.message

    def __str__(self):
        return self.message