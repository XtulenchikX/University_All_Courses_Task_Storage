__all__ = ['print_results']

def print_results(*args, action=None, result=None):
  str_arg = ''
  for some in args:
    str_arg += (str(some) + '   ')
  str_arg = str_arg[:-3]
  str_1 = '◇--' + ('-' * len(str_arg)) + '--◇--' + (
    '-' * len(str(action))) + '--◇--' + ('-' * len(str(result))) + '--◇'
  str_2 = '|  ' + str_arg + '  |  ' + str(action) + '  |  ' + str(
    result) + '  |'
  print(str_1)
  print(str_2)
  print(str_1)
