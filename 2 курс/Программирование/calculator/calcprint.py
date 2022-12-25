import datetime


def write_log(*args, action=None, result=None, file='calc-history.log.txt'):
  """As input, the function receives the values of the arguments, the action, the result, the current date and time, and then writes it to a file that stores the log history.
  """
  f = open(file, mode='a', errors='ignore')
  date = datetime.datetime.today().strftime('%d-%m-%Y %H:%M')
  f.write(f"{date} : {action}: {args} = {result} \n")
  f.close()


def print_results(*args, action=None, result=None):
  """As input, the function receives the values ​​of the arguments, the action and the result, after which it converts the received values into strings and displays the result in the form of a formatted table.
  """
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
