#!/usr/bin/python3

"""
Class Square will create a square at the end and verify everything
"""


class Square:
    """
    Class Square define a new type where you can set the size of your square
    """
# init
    def __init__(self, size=0):
        self.__size = size

# get
    @property
    def size(self):
        return self.__size

# set
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
