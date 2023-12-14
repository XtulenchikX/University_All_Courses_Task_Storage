__all__ = ['calculate']

from .module_stdDev import std_dev
from .module_loadParams import read_params
from .module_convPres import convert_precision

def calculate(op1, op2, action):
  
  PARAMS = read_params()
  
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
