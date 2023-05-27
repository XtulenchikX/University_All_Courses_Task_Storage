from main import std_dev
import unittest


class TestConvertPrecision(unittest.TestCase):

  def test_conPrec(self):
    self.assertEqual(std_dev([1, 1, 1, 1, 1]), 0.0)
    self.assertEqual(std_dev([8,9]), 0.5)
    self.assertEqual(std_dev([21, 15, 16, 20, 18, 19, 17]), 2.0)

if __name__ == '__main__':
  unittest.main()