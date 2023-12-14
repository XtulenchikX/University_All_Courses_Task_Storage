from fib_func import fib
import pytest

def test_fib_1():
  assert fib(1) == [0, 1, 1], "Тривиальный случай n = 1, список [0, 1, 1]"

def test_fib_2():
  assert fib(2) == [0, 1, 1, 2], "fib(2) должно быть [0, 1, 1, 2]"

def test_fib_3():
  assert fib(0) == [0], "fib(0) должно быть [0]"

def test_fib_4():
  assert fib(10) == [0, 1, 1, 2, 3, 5, 8], "fib(10) должно быть [0, 1, 1, 2, 3, 5, 8]"

def test_fib_5():
  assert fib(1000) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987], "fib(1000) должно быть [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]"
