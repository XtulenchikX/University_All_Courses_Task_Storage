def gen_bin_tree_No_rec(height: int, root: int, left_l_func,
                        right_l_func) -> list:
  """The function receives as input the root of a binary tree, the height of the tree, and functions for obtaining the right and left leaves of trees. Then it builds a tree in the form of an array of arrays based on the specified values.
  """
  tree = [[root]]
  if height == 0:
    return tree
  if height == 1:
    return [[root], [[left_l_func(root), right_l_func(root)]]]
  tree = [[root], [[left_l_func(root), right_l_func(root)]]]
  for i in range(height - 1):
    BufList = []

    for el in tree[i + 1]:
      BufListIn = [left_l_func(el[0]), right_l_func(el[0])]
      BufList.append(BufListIn)
      BufListIn = [left_l_func(el[1]), right_l_func(el[1])]
      BufList.append(BufListIn)
    tree.append(BufList)
  return (tree)