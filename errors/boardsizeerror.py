"""
Sample documentation for module.
"""
from errors import ValidationError


class BoardSizeError(ValidationError):
    """
    Represents a configuration error whenever our board is too small
    or too large.
    """

    message: str

    def __init__(self, min_size: int, max_size: int):
        self.message = (f'Board size should be an integer between {min_size} and '
                        f'{max_size} inclusive.')

    def __repr__(self):
        return self.message

    def __str__(self):
        return self.message
