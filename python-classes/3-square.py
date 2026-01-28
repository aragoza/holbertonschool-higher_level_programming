#!/usr/bin/python3

"""
Class Square will create a square at the end and verify everything
"""


class Square:
    """
    Class Square
    """
    def __init__(self, size=0) -> None:
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self) -> int:
        return self.__size * self.__size
