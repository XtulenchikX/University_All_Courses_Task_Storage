#Стецук Максим 2гр.1п.гр.
#Задание 1.1

import random


class RandomNumberIterator:

  def __iter__(self):
    return self

  def __init__(self, num: int, a: int, b: int):
    self.num = num
    self.a = a
    self.b = b
    self.counter = 0

  def __next__(self):
    if self.counter < self.num:
      rnd = random.randint(self.a, self.b)
      self.counter += 1
      return rnd
    else:
      raise StopIteration


num = int(input('Введите количество: '))
a = int(input('Введите нижнюю границу: '))
b = int(input('Введите верхнюю границу: '))

for some in RandomNumberIterator(num, a, b):
  print(some)
