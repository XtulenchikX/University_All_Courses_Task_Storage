import timeit

print('С рекурсией: ', timeit.timeit('gen_bin_tree(height=10, root=11, left_l_func=lambda r: r**2, right_l_func=lambda r: 2 + r**2)', setup="from bin_tree_rec import gen_bin_tree", number = 100))

print('Без рекурсии: ', timeit.timeit('gen_bin_tree_No_rec(height=10, root=11, left_l_func=lambda r: r**2, right_l_func=lambda r: 2 + r**2)', setup="from bin_tree_no_rec import gen_bin_tree_No_rec", number = 100))