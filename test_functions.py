import unittest

from circle import Circle
import math


class TestCircle(unittest.TestCase):
    def test_area(self):
        print(f"Using Circuituous(tm) version { Circle.version}")
        radius = [1, 2, 3]
        circles = [Circle(r) for r in radius]
        area = [c.area() for c in circles]
        area_calculated = [math.pi * r ** 2 for r in radius]
        self.assertEqual(area, area_calculated)

