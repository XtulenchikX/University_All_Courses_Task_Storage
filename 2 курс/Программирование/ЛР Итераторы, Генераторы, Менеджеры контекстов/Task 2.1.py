#Стецук Максим 2гр.1п.гр.
#Задание 2.1

from time import perf_counter


def fibbonachi(count):
  a, b = 0, 1
  for i in range(count):
    yield (a)
    a, b = b, a + b


class Timer:

  def __init__(self):
    self.t_start = 0
    self.t_end = 0

  def __enter__(self):
    self.t_start = perf_counter()

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.t_end = perf_counter()
    self.all_time = self.t_end - self.t_start
    print(self.all_time)
    return False


n = 500000

with Timer():
  for some in fibbonachi(n):
    next(fibbonachi(n))
