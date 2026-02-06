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
        """
        Docstring for __init__

        :param self: Description
        :param width: Description
        :param height: Description
        """
        if width < 0:
            self.width = width
        else:
            raise ValueError
        if height < 0:
            self.height = height
        else:
            raise ValueError

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

    def __init__(self, radius):
        """
        Docstring for __init__

        :param self: Description
        :param radius: Description
        """
        if radius >= 0:
            self.radius = radius
        else:
            raise ValueError

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
