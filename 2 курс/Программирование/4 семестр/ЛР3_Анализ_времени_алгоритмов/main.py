from bin_tree_rec import gen_bin_tree
from bin_tree_no_rec import gen_bin_tree_No_rec


def setup_data(n: int) -> dict:
  """The function receives an integer 'n' as input, creates a dictionary with two keys 'height' and 'root', and then adds 'n' values to each key according to the specified algorithm. And then returns this dictionary.
  """
  data = {'height': [] * n, 'root': [] * n}
  height = 0
  root = 0
  for i in range(n):
    data['height'].append(height)
    data['root'].append(root)
    root += 5
    if (i % 4) == 0:
      height += 1
  return data


def calculate_time(n: int, func, left_l_func, right_l_func) -> float:
  """The function receives an input integer, a function and auxiliary variables that are necessary for the operation of the passed function. Calls a function that creates a variable 'data' (a dictionary of values 'height' and 'root'), and then calculates for each pair of values the start time and end time of work and adds the work time to the array, and then builds a dependency graph from the resulting array.
  """
  import timeit
  data = setup_data(n)
  delta = 0
  for i in range(n):
    height = data['height'][i]
    root = data['root'][i]
    start_time = timeit.default_timer()
    func(height, root, left_l_func, right_l_func)
    delta += timeit.default_timer() - start_time

  return delta


def main():
  import matplotlib.pyplot as plt
  res = []
  for n in range(70):
    res.append(
      calculate_time(n, gen_bin_tree_No_rec, lambda r: r + 3, lambda r: r * 2))
  plt.plot(res)
  plt.show()


if __name__ == "__main__":
  main()
