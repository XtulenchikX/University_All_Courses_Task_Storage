#Стецук Максим 2гр.1п.гр.
#Задание 1.2

import random


def random_number_generator(num, a, b):
  count = 0
  while count < num:
    rnd = random.randint(a, b)
    count += 1
    yield rnd


num = int(input('Введите количество: '))
a = int(input('Введите нижнюю границу: '))
b = int(input('Введите верхнюю границу: '))

for some in random_number_generator(num, a, b):
  print(some)
