from circle import Circle


class Tire(Circle):
    """ Tires are circles with a corrected perimeter"""

    def perimeter(self):
        """ Circumference corrected for rubber"""
        return Circle.__perimeter(self) * 1.25  # a problem if exposing radius

    __perimeter = perimeter

