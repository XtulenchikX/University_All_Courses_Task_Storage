from .module_calcprint import *
from .module_calculate import *
from .module_convPres import *
from .module_loadParams import *
from .module_stdDev import *

# import configparser

# PARAMS = {
#   'precision': None,
#   'output_type': None,
#   'possible_types': None,
#   'dest': None
#   }

__all__ = module_calculate.__all__ + module_calcprint.__all__ + module_stdDev.__all__ + module_convPres.__all__ + module_loadParams.__all__

def calculator_start():
    
  actions_list = ['+', '-', '*', '/', '//', '%', 'std_dev', 'batch_calc']

  action = str(input('Введите действие: '))
  args = []
  if action in actions_list:
    if action == 'std_dev':
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