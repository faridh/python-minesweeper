"""
Helper class to access various constants.
"""


class Constants:
    """
    Helper class to access various constants.
    """

    __reset: str = "\x1b[2K"
    __color_off: str = "\x1b[0m"
    __red: str = "\x1b[31m"
    __green: str = "\x1b[32m"
    __blue: str = "\x1b[34m"

    def __init__(self):
        """
        Empty constructor
        """

    @staticmethod
    def reset() -> str:
        """
        Returns the reset property.
        """
        return Constants.__reset

    @staticmethod
    def color_off() -> str:
        """
        Returns the reset property.
        """
        return Constants.__color_off

    @staticmethod
    def red() -> str:
        """
        Returns the red property.
        """
        return Constants.__red

    @staticmethod
    def green() -> str:
        """
        Returns the red property.
        """
        return Constants.__green

    @staticmethod
    def blue() -> str:
        """
        Returns the red property.
        """
        return Constants.__blue
