#!/usr/bin/python3

"""
Class Shape
"""

from math import pi

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Shape
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Circle
    """

    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        """
        area

        :param self: Description
        """
        return pi * self.radius * self.radius

    def perimeter(self):
        """
        perimeter

        :param self: Description
        """
        return 2 * pi * self.radius


class Rectangle(Shape):
    """
    Rectangle
    """

    def __init__(self, width, height):
        self.width = abs(width)
        self.height = abs(height)

    def area(self):
        """
        area

        :param self: Description
        """
        return self.width * self.height

    def perimeter(self):
        """
        perimeter

        :param self: Description
        """
        return 2 * (self.width + self.height)


def shape_info(self):
    """
    shape_info

    :param self: Description
    """
    print("{}: {}".format("Area", self.area()))
    print("{}: {}".format("perimeter", self.perimeter()))
