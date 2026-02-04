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

    def __str__(self):
        """
        Docstring for __str__

        :param self: Description
        """
        a = self.__class__.__name__
        return "[{}] {}/{}".format(a, self.__width, self.__height)

    def area(self):
        """
        Docstring for area

        :param self: Description
        """
        return self.__width * self.__height
