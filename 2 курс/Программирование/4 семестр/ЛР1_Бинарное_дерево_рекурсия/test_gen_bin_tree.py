from main import gen_bin_tree


def test_gen_bin_tree_smallest():
  assert gen_bin_tree(height=0,
                      root=2,
                      left_l_func=lambda r: r * 2,
                      right_l_func=lambda r: r - 3) == {
                        "2": []
                      }


def test_gen_bin_tree_small():
  assert gen_bin_tree(height=1,
                      root=2,
                      left_l_func=lambda r: r * 2,
                      right_l_func=lambda r: r - 3) == {
                        "2": [{
                          "4": []
                        }, {
                          "-1": []
                        }]
                      }


def test_gen_bin_tree_mid():
  assert gen_bin_tree(height=2,
                      root=2,
                      left_l_func=lambda r: r * 2,
                      right_l_func=lambda r: r - 3) == {
                        "2": [{
                          "4": [{
                            "8": []
                          }, {
                            "1": []
                          }]
                        }, {
                          "-1": [{
                            "-2": []
                          }, {
                            "-4": []
                          }]
                        }]
                      }
