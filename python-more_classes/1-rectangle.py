#!/usr/bin/python3

"""
New class named Rectangle : a rectangle have 4 angle to side parallel
"""


class Rectangle:
    """
    class Rectangle set and get the width and height
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)