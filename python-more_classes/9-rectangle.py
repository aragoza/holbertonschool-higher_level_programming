#!/usr/bin/python3

"""
New class named Rectangle : a rectangle have 4 angle to side parallel
"""


class Rectangle:
    """
    class Rectangle set and get the width and height
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        string = ""
        if a == 0 or b == 0:
            return ""

        for i in range(a - 1):
            for j in range(b):
                if i == a - 1 and j == b:
                    break
                string += "{}".format(self.print_symbol)
            string += '\n'
        for k in range(b):
            string += "{}".format(self.print_symbol)

        return string

# repr
    def __repr__(self):
        a = self.__height
        b = self.__width
        if a == 0 or b == 0:
            return ""
        return "Rectangle({}, {})".format(self.__width, self.__height)

# del
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

# compare 2 rectangle
    def bigger_or_equal(rect1, rect2):
        if not isinstance(rect1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect1.area() >= rect2.area():
            return rect1
        else:
            return rect2

# transform a square into a rectangle
    @classmethod
    def square(cls, size=0):
        return (cls(size, size))
