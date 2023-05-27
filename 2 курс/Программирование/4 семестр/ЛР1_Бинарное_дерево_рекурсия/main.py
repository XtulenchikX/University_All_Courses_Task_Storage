def gen_bin_tree(height: int, root: int, left_l_func, right_l_func) -> dict:
  """The function receives as input the root of a binary tree, the height of the tree, and functions for obtaining the right and left leaves of trees. Then it builds a tree in the form of a dictionary based on the specified values.
  """

  tree = {str(root): []}

  if height == 0:
    return tree
  tree[str(root)].append(
    gen_bin_tree(height - 1,
                 left_l_func(root),
                 left_l_func=left_l_func,
                 right_l_func=right_l_func))
  tree[str(root)].append(
    gen_bin_tree(height - 1,
                 right_l_func(root),
                 left_l_func=left_l_func,
                 right_l_func=right_l_func))
  return tree


if __name__ == '__main__':
  import pprint

  pprint.pprint(
    gen_bin_tree(height=3,
                 root=11,
                 left_l_func=lambda r: r**2,
                 right_l_func=lambda r: 2 + r**2))
