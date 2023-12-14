__all__ = ['convert_precision']

def convert_precision(x):
  x = float(x)
  authenticity = 0
  while x < 1:
    authenticity += 1
    x = x * 10
  return authenticity