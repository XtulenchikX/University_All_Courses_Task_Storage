import functools
import json


def memoized(func):
  '''
  This function acts as a decorator to store the results of a given func. It also looks for the result of executing the func function from the passed value in the cache, so as not to perform repeated calculations.
  '''
  _cache = {}

  @functools.wraps(func)
  def inner(*args, **kwargs):
    key = f'{args[0]}, {func.__name__}'
    if key not in inner.cache:
      inner.cache[key] = func(*args, **kwargs)
    return inner.cache[key]

  inner.cache = _cache
  return inner


@memoized
def factorial1(n):
  '''
  The function finds the factorial of a number using the corresponding function from the Math package
  '''
  from math import factorial
  return factorial(n)


@memoized
def factorial2(n):
  '''
  The function finds the factorial of a number using the corresponding function from the scipy package
  '''
  from scipy.special import factorial
  return factorial(n)


def save_to_cache(filename, cache):
  '''
  The function saves the data passed to it to the specified file.
  '''
  with open(filename, "w") as f:
    json.dump(cache, f)


def load_from_cache(filename):
  '''
  The function loads data from the specified file.
  '''
  try:
    with open(filename, "r") as f:
      return json.load(f)
  except FileNotFoundError:
    return {}
