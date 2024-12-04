import unittest

import triangle


class TriangleTestCase(unittest.TestCase):
    def test_zero_size_area(self):
        area = triangle.area(0, 1)
        self.assertEqual(area, 0)
        area = triangle.area(1, 0)
        self.assertEqual(area, 0)

    def test_positive_size_area(self):
        area = triangle.area(3, 6)
        self.assertEqual(area, 9)
        area = triangle.area(5, 10)
        self.assertEqual(area, 25)
        area = triangle.area(10.5, 4)
        self.assertEqual(area, 21)

    def test_negative_size_ares(self):
        with self.assertRaises(Exception):
            triangle.area(-10, -1)

        with self.assertRaises(Exception):
            triangle.area(10, -1)

        with self.assertRaises(Exception):
            triangle.area(-10, 1)

    def test_zero_size_perimeter(self):
        perimeter = triangle.perimeter(0, 1, 2)
        self.assertEqual(perimeter, 3)

    def test_positive_size_perimeter(self):
        perimeter = triangle.perimeter(3, 4, 5)
        self.assertAlmostEqual(perimeter, 12)
        perimeter = triangle.perimeter(5, 7, 10)
        self.assertAlmostEqual(perimeter, 22)
        perimeter = triangle.perimeter(10.5, 10.5, 10.5)
        self.assertAlmostEqual(perimeter, 31.5)

    def test_negative_size_perimeter(self):
        with self.assertRaises(Exception):
            triangle.perimeter(-10, 2, 3)

        with self.assertRaises(Exception):
            triangle.perimeter(10, -2, 3)

        with self.assertRaises(Exception):
            triangle.perimeter(10, 2, -3)

        with self.assertRaises(Exception):
            triangle.perimeter(10, -2, -3)

        with self.assertRaises(Exception):
            triangle.perimeter(-10, 2, -3)

        with self.assertRaises(Exception):
            triangle.perimeter(-10, -2, -3)

    def test_unable_size_perimeter(self):
        with self.assertRaises(Exception):
            triangle.perimeter(10, 2, 3)

        with self.assertRaises(Exception):
            triangle.perimeter(2, 10, 3)

        with self.assertRaises(Exception):
            triangle.perimeter(2, 3, 10)
