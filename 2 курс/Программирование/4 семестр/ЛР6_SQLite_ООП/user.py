import re

class Users:
  def __init__(self, name : str, height : float, created : str):
    if Users.__check_name(self, name): self.__name = name
    if Users.__check_height(self, height): self.__height = height
    if Users.__check_created(self, created): self.__created = created
  
  @property
  def name(self):
        return self.__name

  @name.setter
  def name(self, name):
    if Users.__check_name(self, name): self.__name = name

  @name.deleter
  def name(self):
      self.__name = None
       
  @property
  def height(self):
        return self.__height

  @height.setter
  def height(self, height):
    if Users.__check_height(self, height): self.__height = height

  @height.deleter
  def height(self):
        self.__height = None

  @property
  def created(self):
    return self.__created

  @created.setter
  def created(self, created):
    if Users.__check_created(self, created): self.__created = created

  @created.deleter
  def created(self):
    self.__created = None

  def __check_name(self, name):
    """
    This function gets the value name and checks for correctness.
    """
    if (name[0] not in ['0','1','2','3','4','5','6','7','8','9']) and (name != None):
      return True
    else:
      raise ValueError('Error with name! Try again...')
    
  def __check_height(self, height):
    """
    This function gets the value height and checks for correctness.
    """
    if (height > 1):
      return True
    else:
      raise ValueError('Error with height! Try again...')
    
  def __check_created(self, created):
    """
    This function gets the value created and checks for correctness.
    """
    if re.match('\d{4}-\d\d-\d\d \d\d:\d\d:\d\d', created):
      return True
    else:
      raise ValueError('Error with created DateTime! Try again...')