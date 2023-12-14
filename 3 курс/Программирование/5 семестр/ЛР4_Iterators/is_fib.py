class FibonacchiLst:
    def __init__(self, list):
      self.list = list
      self.idx = 0
      
    def __iter__(self):
      return self

    def __next__(self):
      from fib_func import fib
      max_el = max(self.list)
      self.iterable = fib(max_el+1)
      while True:
        try:
          res = self.list[self.idx]
        except IndexError:
          raise StopIteration
        if res in self.iterable:
          self.idx += 1
          return res
        self.idx += 1