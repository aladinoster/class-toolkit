import unittest

from circle import Circle
from tire import Tire

import math
from random import random, seed


class TestCircle(unittest.TestCase):
    def test_area(self):
        print(f"Using Circuituous(tm) version { Circle.version}")
        radius = [1, 2, 3]
        circles = [Circle(r) for r in radius]
        area = [c.area() for c in circles]
        area_calculated = [math.pi * r ** 2 for r in radius]
        self.assertEqual(area, area_calculated)


class TestRandomCircle(unittest.TestCase):
    def test_creation_n_circles(self):
        seed(8675309)
        print(f"Using Circuituous(tm) version {Circle.version}")
        n = 10
        radius = [random() for _ in range(n)]
        circles = [Circle(r) for r in radius]
        print(f"The average area of {n} random circles is")
        avg_area = sum([c.area() for c in circles]) / n
        print(f"is {avg_area:.1f}")
        avg_area_calculated = sum([math.pi * r ** 2 for r in radius]) / n
        self.assertEqual(avg_area, avg_area_calculated)


class TestExposureParameters(unittest.TestCase):
    def test_modify_radius_after_creation(self):
        cuts = [0.1, 0.7, 0.8]
        circles = [Circle(r) for r in cuts]
        for c in circles:
            print(f"A circle with a radius {c.radius}")
            print(f"has a perimeter of {c.perimeter()}")
            print(f"and a cold area of {c.area()}")
            c.radius *= 1.1
            print(f"and a warm area of {c.area()}")
            self.assertEqual(c.area(), math.pi * c.radius ** 2)


class TestTires(unittest.TestCase):
    def test_new_usage_circles(self):
        t = Tire(22)
        print(f"A tire of radius {t.radius}")
        print(f"has an inner area of {t.area()}")
        print(f"and an odometer perimeter of {t.perimeter()}")
        self.assertEqual(t.perimeter(), 22 * math.pi * 2 * 1.25)


class TestConstructor(unittest.TestCase):
    def test_new_constructor(self):
        def bbd_to_radius(bbd):
            return bbd / 2.0 / math.sqrt(2.0)  # from bounding box to radius

        bbd = 25.1
        c = Circle(bbd_to_radius(bbd))
        print(f"A circle with bbd {bbd}")
        print(f"has a radius ouf {c.radius}")
        print(f"an area of {c.area()} and perimeter {c.perimeter()}")
        c_new = Circle.frombbd(bbd)
        self.assertEqual(c_new.radius, c.radius)

