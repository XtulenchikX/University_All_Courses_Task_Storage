#Стецук Максим 2гр.1п.гр.
#Задание 2.2

__settings = {'precision': '0.000001'}


def convert_precision(x):
  x = float(x)
  authenticity = 0
  while x < 1:
    authenticity += 1
    x = x * 10
  return authenticity


def std_dev(op1):
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
  global __settings

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

  return round(result, convert_precision(__settings.get('precision')))


class BatchCalculatorContexManager(object):

  def __init__(self, name, method):
    self.file = open(name, method)

  def __enter__(self):
    return self.file

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.file.close()


def BatchCalc():

  with BatchCalculatorContexManager('Task2.2ex', 'r') as file:
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
  global __settings

  action = input('Введите действие: ')

  if action == 'batch_calc':
    BatchCalc()
    quit()

  if action == 'std_dev':
    operand1 = []
    op = 1
    while op != "":
      op = input("Введите операнд: ")
      if op == "":
        break
      else:
        op = float(op)
        operand1.append(op)
    operand2 = 0
  else:
    operand1 = float(input('Введите операнд 1: '))
    operand2 = float(input('Введите операнд 2: '))

  res = calculate(operand1, operand2, action)

  print(res)


if __name__ == '__main__':
  main()
