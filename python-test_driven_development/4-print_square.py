#!/usr/bin/python3
"""
Module that defines a function to print a square using the character '#'.

The square has a size equal to the given integer argument. Each row and
column contains exactly `size` number of '#' characters.
"""


def print_square(size):
    """
    Prints a square with the character '#'.

    The size of the square is determined by the value of `size`. Each row
    and each column of the square is composed of `size` number of '#'
    characters.

    Args:
        size (int): the size length of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if type(size) is float and size < 0:
        raise TypeError("div must be a number")

    if type(size) is not int:
        raise TypeError("div must be a number")
    
    if size < 0:
        raise ValueError("size must be >= 0")


    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
