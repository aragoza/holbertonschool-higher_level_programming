#!/usr/bin/python3
"""Rectangle
Init of the attribute width and height
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
