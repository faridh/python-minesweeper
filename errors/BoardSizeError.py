from errors.ValidationError import ValidationError


class BoardSizeError(ValidationError):

    message: str

    def __init__(self, min, max):
        self.message = f'Board size should be an integer between {min} and {max} inclusive.'

    def __repr__(self):
        return self.message

