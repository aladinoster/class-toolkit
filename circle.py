""" Circuitous 
    An advanced circle analytics company

"""
import math


class Circle(object):
    "An advanced circle analytic toolkit"

    version = "0.2"

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2.0

    def perimeter(self):
        return 2.0 * math.pi * self.radius