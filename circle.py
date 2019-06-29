""" Circuitous 
    An advanced circle analytics company

"""
import math


class Circle(object):
    "An advanced circle analytic toolkit"

    version = "0.4"

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2.0

    def perimeter(self):
        return 2.0 * math.pi * self.radius

    @classmethod
    def frombbd(cls, bbd):
        "Constructs the circle from the bounding box"
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)  # This can now be used by tire properly

    @staticmethod
    def angle_to_grade(angle):
        "Convert angle to in degree to percentage grade"
        return math.tan(math.radians(angle)) * 100.0
