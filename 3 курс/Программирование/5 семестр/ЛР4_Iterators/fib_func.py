def fib(n:int):
  a = 1
  b = 0
  if n < 0:
    raise ValueError("n positive or zero")
  if n == 0:
    return [b]
  else:
    fib_list = [b, a]
    for i in range(1, n+1, 1):
      if (i == a + b):
        fib_list.append(i)
        b = a
        a = i
    return fib_list