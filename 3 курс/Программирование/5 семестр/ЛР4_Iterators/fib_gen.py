def fibonacci_gen():
  b, a = 0, 1
  while True:
      yield b
      b, a = a, a + b