from typing import Optional, List

from errors.BoardSizeError import BoardSizeError
from errors.NumberOfMinesError import NumberOfMinesError

class Validator:

  min_board_size = 4
  max_board_size = 20

  @staticmethod
  def get_configuration_errors(board_size: int, number_of_mines: int) -> List[Optional[type]]:
    errors = []
    if not Validator.__valid_board_size(board_size):
      errors.append(BoardSizeError(Validator.min_board_size, Validator.max_board_size))
      return errors

    board_size = int(board_size)
    if not Validator.__valid_number_of_mines(board_size, number_of_mines):
      min_mines = Validator.__min_valid_mines(board_size)
      max_mines = Validator.__max_valid_mines(board_size)
      errors.append(NumberOfMinesError(min_mines, max_mines))
    return errors
  
  @staticmethod
  def __valid_board_size(board_size: int) -> bool:
    if not Validator.__is_integer(board_size):
      return False
  
    board_size = int(board_size)
    if not Validator.min_board_size <= board_size <= Validator.max_board_size:
      return False
    return True
  
  @staticmethod
  def __valid_number_of_mines(board_size: int, number_of_mines: int) -> bool:
    board_size = int(board_size)  
    if not Validator.__is_integer(number_of_mines):
      return False
    
    number_of_mines = int(number_of_mines)
    min_mines = Validator.__min_valid_mines(board_size)
    max_mines = Validator.__max_valid_mines(board_size)
    if not min_mines <= number_of_mines <= max_mines:
      return False

    return True

  @staticmethod
  def __is_integer(input) -> bool:
    try:
        int(input)
    except ValueError:
        return False
    return True

  @staticmethod
  def is_in_range(value: type, size: int) -> bool:
    if not Validator.__is_integer(value):
      return False
    value = int(value)
    if value not in range(0, size):
      return False
    return True

  @staticmethod
  def __min_valid_mines(board_size: int) -> int:
    return board_size // 2

  @staticmethod
  def __max_valid_mines(board_size: int) -> int:
    return board_size ** 2 // 4 # ~25 % total cells
  
