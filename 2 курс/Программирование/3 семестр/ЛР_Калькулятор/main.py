# Лабораторная работа "Тестирование"
# Автор: Стецук Максим

import configparser

from calcprint import write_log
from calcprint import print_results

PARAMS = {
  'precision': None,
  'output_type': None,
  'possible_types': None,
  'dest': None
}


def read_params():
  """ The function reads the params.ini file and gets the values for the PARAMS settings dictionary keys.
  """
  config = configparser.ConfigParser()
  config.read('params.ini')
  return config


def convert_precision(x):
  """Converts a string to an float and then obtains the rounding precision in characters from that number.
  
  >>> convert_precision('0.000001')
  6
  
  >>> convert_precision('0.0001')
  4
  
  >>> convert_precision('0.001')
  3
  """

  x = float(x)
  authenticity = 0
  while x < 1:
    authenticity += 1
    x = x * 10
  return authenticity


def std_dev(op1):
  """Takes as input any number of elements that are written to the array, and then calculates the standard deviation
  
  >>> std_dev([1, 1, 1, 1])
  0.0

  >>> std_dev([4,5])
  0.5

  >>> std_dev([8, 6, 7, 5, 9, 10, 11])
  2.0
  """
  import math
  res = 0
  average = 0
  for i in range(0, len(op1)):
    average += op1[i]
  average = average / (len(op1))
  for i in range(0, len(op1)):
    res = res + (op1[i] - average)**2
  res = res * 1 / (len(op1))
  res = math.sqrt(res)

  return res


def calculate(op1, op2, action):
  global PARAMS
  """As input, the function first receives an action, from which it calculates the required expression with the corresponding operation
  
  >>> calculate(7, 9, '-')
  -2

  >>> calculate(15, 6, '//')
  2

  >>> calculate(83, 3, '%')
  2
  """
  if action == '+':
    result = op1 + op2
  elif action == '-':
    result = op1 - op2
  elif action == '*':
    result = op1 * op2
  elif action == '/':
    if op2 == 0:
      print('На ноль не поделить')
      return
    else:
      result = op1 / op2
  elif action == '//':
    result = op1 // op2
  elif action == '%':
    result = op1 % op2
  elif action == 'std_dev':
    result = std_dev(op1)

  return round(result, convert_precision(PARAMS['precision']))


class BatchCalculatorContexManager(object):

  def __init__(self, name, method):
    self.file = open(name, method)

  def __enter__(self):
    return self.file

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.file.close()


def BatchCalc():
  """
  The function reads the lines of the file, which are expressions to be evaluated. Splits strings by operand and calls the "calculate" function for each string. And then displays each expression with the result on the screen.
  """

  with BatchCalculatorContexManager('ExpressionsForBCCM', 'r') as file:
    mass = []
    for line in file:
      mass.append(line.replace('\n', ''))

  def calc_gen(mass):
    for el in mass:
      for char in el:
        if char == '+':
          action = '+'
          m_buf = el.split('+')
          op1 = int(m_buf[0])
          op2 = int(m_buf[1])
          yield el + ' = ' + str(calculate(op1, op2, action))
        elif char == '-':
          action = '-'
          m_buf = el.split('-')
          op1 = int(m_buf[0])
          op2 = int(m_buf[1])
          yield el + ' = ' + str(calculate(op1, op2, action))
        elif char == '*':
          action = '*'
          m_buf = el.split('*')
          op1 = int(m_buf[0])
          op2 = int(m_buf[1])
          yield el + ' = ' + str(calculate(op1, op2, action))
        elif char == '%':
          action = '%'
          m_buf = el.split('%')
          op1 = int(m_buf[0])
          op2 = int(m_buf[1])
          yield el + ' = ' + str(calculate(op1, op2, action))
        elif char == '/':
          i = el.index('/')
          if el[i + 1] == '/':
            action = '//'
            m_buf = el.split('//')
            op1 = int(m_buf[0])
            op2 = int(m_buf[1])
            yield el + ' = ' + str(calculate(op1, op2, action))
          else:
            action = '/'
            m_buf = el.split('/')
            op1 = int(m_buf[0])
            op2 = int(m_buf[1])
            yield el + ' = ' + str(calculate(op1, op2, action))

  for some in calc_gen(mass):
    print(some)


def main():

  global PARAMS

  config = read_params()
  PARAMS['precision'] = config['settings']['precision']
  PARAMS['output_type'] = config['settings']['output_type']
  PARAMS['possible_types'] = config['settings']['possible_types']
  PARAMS['dest'] = config['settings']['dest']

  actions_list = ['+', '-', '*', '/', '//', '%', 'std_dev', 'batch_calc']

  action = str(input('Введите действие: '))
  args = []
  if action in actions_list:
    if action == 'batch_calc':
      BatchCalc()
      quit()
    elif action == 'std_dev':
      operand1 = []
      op = 1
      while op != "":
        op = input("Введите операнд: ")
        if op == "":
          break
        else:
          try:
            op = float(op)
          except ValueError:
            print('Ошибка: Введено не число!\n')
            quit()
          operand1.append(op)
          args.append(op)
      operand2 = 0
    else:
      try:
        operand1 = float(input('Введите операнд 1: '))
        operand2 = float(input('Введите операнд 2: '))
      except ValueError:
        print('Ошибка: Введено не число!\n')
        quit()
      args.append(operand1)
      args.append(operand2)
  else:
    print('Вы допустили ошибку при вводе действия!\n'
          'Доступные действия: +, -, *, /, //, %, std_dev, batch_calc.\n')
    quit()

  res = calculate(operand1, operand2, action)

  print_results(*args, action=action, result=res)

  write_log(*args, action=action, result=res)


if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
