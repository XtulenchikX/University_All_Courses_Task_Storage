from main import gen_bin_tree_No_rec


def test_gen_bin_tree_No_rec_smallest():
  assert gen_bin_tree_No_rec(height=0,
                      root=3,
                      left_l_func=lambda r: r**2,
                      right_l_func=lambda r: r + 7) == [[3]]


def test_gen_bin_tree_No_rec_small():
  assert gen_bin_tree_No_rec(height=1,
                      root=3,
                      left_l_func=lambda r: r**2,
                      right_l_func=lambda r: r + 7) == [[3], [[9, 10]]]


def test_gen_bin_tree_No_rec_mid():
  assert gen_bin_tree_No_rec(height=2,
                      root=3,
                      left_l_func=lambda r: r**2,
                      right_l_func=lambda r: r + 7) == [[3], [[9, 10]], [[81, 16], [100, 17]]]
