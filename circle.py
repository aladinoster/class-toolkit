""" Circuitous 
    An advanced circle analytics company

"""
import math


class Circle(object):
    "An advanced circle analytic toolkit"

    version = "0.6"

    # flyweight pattern
    __slots__ = ["diameter"]  # No dict, no adding attributes (impr. efficiency)

    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self.__perimeter() / math.pi / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2

    def area(self):
        p = self.__perimeter()  # This calls only circle's perimeter
        r = p / math.pi / 2.0
        return math.pi * r ** 2.0

    def perimeter(self):
        return 2.0 * math.pi * self.radius

    __perimeter = perimeter  # This creates _Circle_perimeter

    @classmethod
    def frombbd(cls, bbd):
        "Constructs the circle from the bounding box"
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)  # This can now be used by tire properly

    @staticmethod
    def angle_to_grade(angle):
        "Convert angle to in degree to percentage grade"
        return math.tan(math.radians(angle)) * 100.0
