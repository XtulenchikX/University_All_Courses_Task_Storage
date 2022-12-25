#Стецук Максим 2гр.1п.гр.
#Задание 1.3


def fibonacci(n):
  a = b = 1
  for i in range(n):
    yield a
    a, b = b, a + b


def plus_ten(x):
  for num in x:
    num += 10
    yield num


n = int(input('Введите количество:'))
fib = fibonacci(n)
for some in plus_ten(fib):
  print(some)
