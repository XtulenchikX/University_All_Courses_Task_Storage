from main import convert_precision
import unittest


class TestConvertPrecision(unittest.TestCase):

  def test_conPrec(self):
    self.assertEqual(convert_precision('0.000000001'), 9)
    self.assertEqual(convert_precision('0.00001'), 5)
    self.assertEqual(convert_precision('0.0000000000000001'), 16)

if __name__ == '__main__':
  unittest.main()