import unittest

import square

class squareTestCase(unittest.TestCase):
    def test_zero_size_area(self):
        area = square.area(0)
        self.assertEqual(area, 0)
    
    def test_positive_size_area(self):
        area = square.area(3)
        self.assertEqual(area, 9)
        area = square.area(5)
        self.assertEqual(area, 25)
        area = square.area(10.5)
        self.assertEqual(area, 110.25)
    
    def test_negative_size_ares(self):
        with self.assertRaises(Exception):
            square.area(-10)

    def test_zero_size_perimeter(self):
        perimeter = square.perimeter(0)
        self.assertEqual(perimeter, 0)
    
    def test_positive_size_perimeter(self):
        perimeter = square.perimeter(3)
        self.assertAlmostEqual(perimeter, 12)
        perimeter = square.perimeter(5)
        self.assertAlmostEqual(perimeter, 20)
        perimeter = square.perimeter(10.5)
        self.assertAlmostEqual(perimeter, 42)
    
    def test_negative_size_perimeter(self):
        with self.assertRaises(Exception):
            square.perimeter(-10)
