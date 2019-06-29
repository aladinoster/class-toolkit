""" Circuitous 
    An advanced circle analytics company

"""


class Circle(object):  # A new style class
    "An advanced circle analytic toolkit"

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2.0
