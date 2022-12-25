from main import calculate
import unittest


class TestCalculate(unittest.TestCase):

  def test_sum(self):
    self.assertEqual(calculate(758, 247, '+'), 1005)
    self.assertIs(type(calculate(2, 3, '+')), int)

  def test_minus(self):
    self.assertEqual(calculate(789, 457, '-'), 332)
    self.assertEqual(calculate(457, 789, '-'), -332)

  def test_multiply(self):
    self.assertEqual(calculate(77, 13, '*'), 1001)
    self.assertEqual(calculate(-7, -8, '*'), 56)
    self.assertEqual(calculate(164, 0, '*'), 0)

  def test_division(self):
    self.assertEqual(calculate(784, 19, '/'), 41.263158)
    self.assertIsNone(calculate(7, 0, '/'))

  def test_intDiv(self):
    self.assertEqual(calculate(1008, 11, '//'), 91)
    self.assertEqual(calculate(17.5, 2, '//'), 8)

  def test_ostat(self):
    self.assertEqual(calculate(1008, 11, '%'), 7)
    self.assertEqual(calculate(17.5, 2, '%'), 1.5)

  def test_StdDev(self):
    self.assertEqual(calculate([4, 5], 0, 'std_dev'), 0.5)
    self.assertEqual(calculate([1, 2, 3, 4, 5, 6, 7], 0, 'std_dev'), 2)
    self.assertEqual(calculate([7, 2, 1, 8, 16], 0, 'std_dev'), 5.344156)

if __name__ == '__main__':
  unittest.main()
