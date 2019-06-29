""" Circuitous 
    An advanced circle analytics company

"""
import math

class Circle(object):
    "An advanced circle analytic toolkit"

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2.0