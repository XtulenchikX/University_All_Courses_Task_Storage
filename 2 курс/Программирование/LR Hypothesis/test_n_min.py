from n_min import n_min
import pytest
from hypothesis import given
import hypothesis.strategies as st


@pytest.mark.parametrize(
  "inp_lst, numOf, expected",
  [([-81, -11, -10, -8, -7, -2, -1, 1, 2, 3, 4, 6, 14, 18, 18, 63
     ], 4, -1653372),
   ([-9, 8, -7, 5, -4, -3, 4, -5, 10, 7, -8, 9, 6, 11], 6, -498960),
   ([-19, -8, -8, -8, -6, 0, 1, 3, 4, 15, 17, 27, 37], 5, -4840155),
   ([-10, -8, -1, 5, 6, 9], 3, -540)])
def test_simple_hypo(inp_lst, numOf, expected):
  assert n_min(inp_lst, numOf) == expected


@given(inp_lst=st.lists(st.integers()), numOf=st.integers())
def test_result_typo_hypo(inp_lst, numOf):
  """Checks that the function outputs an integer regardless of the number of list items and the required number of items in the product.
  """
  if numOf > 0 and numOf <= len(inp_lst):
    assert isinstance(n_min(inp_lst, numOf), int)


@given(inp_lst=st.lists(st.integers()))
def test_sort_fun_hypo(inp_lst):
  """Checks the correctness of the sort function by comparing the result of its operation with the bubble method.
  """
  inp_lst_buf = inp_lst
  inp_lst.sort()
  length = len(inp_lst)
  for i in range(length - 1):
    for j in range(length - i - 1):
      if inp_lst_buf[j] > inp_lst_buf[j + 1]:
        inp_lst_buf[j], inp_lst_buf[j + 1] = inp_lst_buf[j + 1], inp_lst_buf[j]
  assert inp_lst == inp_lst_buf
