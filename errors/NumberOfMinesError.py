class NumberOfMinesError:
  
  message: str

  def __init__(self, min, max):
    self.message = f'Number of mines should be an integer between {min} and {max} inclusive.'

  def __repr__(self):
    return self.message

