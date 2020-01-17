import unittest

import zstat

class TestZstat(unittest.TestCase):
  def empty_input_returns_None(self):
    inputs = []
    percentiles = [50]
    outputs = zstat.get_percentiles(inputs, percentiles)
    self.assertIsNone(outputs)


  def one_input_returns_one_input(self):
    inputs = [100]
    percentiles = [50]
    outputs = zstat.get_percentiles(inputs, percentiles)
    self.assertEqual(outputs, [(50, 100)])


  def small_percentile_returns_first_odd(self):
    inputs = [1, 2, 3, 4, 5]
    percentiles = [0]
    outputs = zstat.get_percentiles(inputs, percentiles)
    self.assertEqual(outputs, [(0, 1)])


  def small_percentile_returns_first(self):
    inputs = [1, 2, 3, 4]
    percentiles = [0]
    outputs = zstat.get_percentiles(inputs, percentiles)
    self.assertEqual(outputs, [(0, 1)])


  def test_input_small(self):
    inputs = [456, 366, 695, 773, 617, 826, 56, 78, 338, 326]
    percentiles = [50, 90, 100]
    outputs = zstat.get_percentiles(inputs, percentiles)
    self.assertEqual(
            outputs, [
                (50, 366),
                (90, 773),
                (100, 826)
            ]
    )


  def test_input_small(self):
    inputs = [456, 366, 695, 773, 617, 826, 56, 78, 338, 326]
    percentiles = [0, 50]
    outputs = zstat.get_percentiles(inputs, percentiles)
    self.assertEqual(
            outputs, [
                (0, 56),
                (50, 366)
            ]
    )


  def test_input_small_decimal_percentiles(self):
    inputs = [456, 366, 695, 773, 617, 826, 56, 78, 338, 326]
    percentiles = [99.0, 99.9, 99.99999]
    outputs = zstat.get_percentiles(inputs, percentiles)
    self.assertEqual(
            outputs, [
                (99.0, 826),
                (99.9, 826),
                (99.99999, 826)
            ]
    )


if __name__ == '__main__':
  unittest.main()

