__all__ = ['std_dev']

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