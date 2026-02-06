#!/usr/bin/python3

"""
3 Class 1 base class and 2 subclass
"""


from abc import ABC, abstractmethod


from math import pi


class Shape(ABC):
    """
    Class Shape
    """

    @abstractmethod
    def area(self):
        """
        Docstring for area

        :param self: Description
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Docstring for perimeter

        :param self: Description
        """
        pass


class Rectangle(Shape):
    """
    Class Rectangle
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Docstring for area

        :param self: Description
        """
        return self.width * self.height

    def perimeter(self):
        """
        Docstring for perimeter

        :param self: Description
        """
        return 2 * (self.width + self.height)


class Circle(Shape):
    """
    Class Circle
    """

    def __init__(self, radius > 0):
        self.radius = radius

    def area(self):
        """
        Docstring for area

        :param self: Description
        """
        return pi * (self.radius ** 2)

    def perimeter(self):
        """
        Docstring for perimeter

        :param self: Description
        """
        return 2 * pi * self.radius


def shape_info(self):
    """
    Docstring for shape_info

    :param self: Description
    """
    print("Area: {}".format(self.area()))
    print("Perimeter: {}".format(self.perimeter()))
