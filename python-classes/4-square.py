#!/usr/bin/python3

"""
Class Square will create a square at the end and verify everything
"""


class Square:
    """
    Class Square
    """
    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    def size(self, value: int):
        self.size = value

    def size(self: int) -> int:
        return self.size
    
    def area(self: int) -> int:
        if not isinstance(self.size, int):
            raise TypeError("size must be an integer")
        return self.size * self.size
