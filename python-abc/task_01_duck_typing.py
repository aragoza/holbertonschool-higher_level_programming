#!/usr/bin/python3

"""
Docstring for holbertonschool-higher_level_programming.python-abc.task_00_abc
"""

from math import pi

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Docstring for Shape
    """

    @abstractmethod
    def area(self):
        ...

    @abstractmethod
    def perimeter(self):
        ...


class Circle(Shape):
    """
    Docstring for Circle
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Docstring for area
        
        :param self: Description
        """
        return pi * self.radius * self.radius

    def perimeter(self):
        """
        Docstring for perimeter
        
        :param self: Description
        """
        return 2 * pi * self.radius


class Rectangle(Shape):
    """
    Docstring for Rectangle
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


def shape_info(self):
    """
    Docstring for shape_info
    
    :param self: Description
    """
    print("{}: {}".format("Area", self.area()))
    print("{}: {}".format("perimeter", self.perimeter()))
