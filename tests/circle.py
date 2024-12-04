import unittest

import circle


class CircleTestCase(unittest.TestCase):
    def test_zero_radius_area(self):
        area = circle.area(0)
        self.assertEqual(area, 0)

    def test_positive_radius_area(self):
        area = circle.area(3)
        self.assertAlmostEqual(area, 28.27433388)
        area = circle.area(5)
        self.assertAlmostEqual(area, 78.53981634)
        area = circle.area(10.5)
        self.assertAlmostEqual(area, 346.36059006)

    def test_negative_radius_ares(self):
        with self.assertRaises(Exception):
            circle.area(-10)

    def test_zero_radius_perimeter(self):
        perimeter = circle.perimeter(0)
        self.assertEqual(perimeter, 0)

    def test_positive_radius_perimeter(self):
        perimeter = circle.perimeter(3)
        self.assertAlmostEqual(perimeter, 18.84955592)
        perimeter = circle.perimeter(5)
        self.assertAlmostEqual(perimeter, 31.41592654)
        perimeter = circle.perimeter(10.5)
        self.assertAlmostEqual(perimeter, 65.97344573)

    def test_negative_radius_perimeter(self):
        with self.assertRaises(Exception):
            circle.perimeter(-10)
