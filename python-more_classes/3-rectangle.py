#!/usr/bin/python3

"""
New class named Rectangle : a rectangle have 4 angle to side parallel
"""


class Rectangle:
    """
    class Rectangle set and get the width and height
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

# get
    @property
    def width(self):
        return self.__width

# set
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

# get
    @property
    def height(self):
        return self.__height

# set
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

# area
    def area(self):
        return self.__width * self.__height

# perimeter
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((2 * self.__height) + (2 * self.__width))

# str
    def __str__(self):
        a = self.__height
        b = self.__width
        if a == 0 or b == 0:
            return ""
        return ("#" * b + "\n") * (a - 1) + "#" * b
