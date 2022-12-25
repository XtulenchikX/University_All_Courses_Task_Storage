def n_min(lst: list, n):
  length = len(lst)
  lst.sort()
  print('Отсортированный массив: ', lst)
  if lst[0] >= 0:
    res = 1
    i = 0
    while i < n:
      res *= lst[i]
      i += 1
    return res
  else:
    new_lst = []
    for i in range(n):
      res = 1
      for k in range(i + 1):
        res *= lst[k]
      for j in range(length - n + i + 1, length):
        res *= lst[j]
      new_lst.append(res)
      i += 1
    result = min(new_lst)
    return result
