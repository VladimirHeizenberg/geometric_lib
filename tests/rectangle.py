import unittest

import rectangle

class RectangleTestCase(unittest.TestCase):
    def test_zero_sizes_ares(self):
        area = rectangle.area(0, 0)
        self.assertEqual(area, 0)
        area = rectangle.area(0, 10)
        self.assertEqual(area, 0)
        area = rectangle.area(10, 0)
        self.assertEqual(area, 0)
    
    def test_positive_sizes_area(self):
        area = rectangle.area(1, 1)
        self.assertEqual(area, 1)
        area = rectangle.area(1, 10)
        self.assertEqual(area, 10)
        area = rectangle.area(10, 1)
        self.assertEqual(area, 10)
        area = rectangle.area(5, 4)
        self.assertEqual(area, 20)
        area = rectangle.area(123, 4243)
        self.assertEqual(area, 521889)
        area = rectangle.area(566.2, 12.6)
        self.assertAlmostEqual(area, 7134.12)
    
    def test_negative_sizes_area(self):
        with self.assertRaises(Exception):
            rectangle.area(-10, 5)

        with self.assertRaises(Exception):
            rectangle.area(5, -10)

        with self.assertRaises(Exception):
            rectangle.area(-10, -20)
