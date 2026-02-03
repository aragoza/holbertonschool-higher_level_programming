#!/usr/bin/python3
"""Rectangle
whole class rectangle with attribute width and height
and the method area and str for human representation
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Class Rectangle
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    
    def area(self):
        return self.__width * self.__height
    