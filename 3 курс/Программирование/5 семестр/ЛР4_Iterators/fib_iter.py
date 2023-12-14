def fib_iter(list_range):
  from fib_func import fib
  from itertools import filterfalse

  fibs_in_list = list(filterfalse(lambda x: not (x in fib(x)), list_range))

  return fibs_in_list

  