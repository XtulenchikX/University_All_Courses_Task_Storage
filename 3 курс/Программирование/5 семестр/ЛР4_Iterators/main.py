def main():
  # task 1
  # from fib_func import fib
  # n = int(input('n = '))
  # print(fib(n))

  # task 2
  # from is_fib import FibonacchiLst
  # print(list(FibonacchiLst([1,2,3,4,5,1,1,1,8,9,11,13,])))

  # task 3
  # from fib_iter import fib_iter
  # # print(fib_iter([1,2,3,4,5,1,1,1,8,9,11,13]))
  # print(fib_iter(range(100)))

  # task 4
  from fib_gen import fibonacci_gen
  from itertools import islice
  fib_gener = fibonacci_gen()
  list_of_fib = list(islice(fib_gener, 20))
  print(list_of_fib)
      


if __name__ == "__main__":
  main()