#!/usr/bin/python3
"""BaseGeometry
class that have an area and an integer validator method
"""


class BaseGeometry():
    """
    class that verify the type of every attribute passed in parameter
    """

    def area(self):
        """
        Docstring for area

        :param self: Description
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Docstring for integer_validator

        :param self: Description
        :param name: Description
        :param value: Description
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
