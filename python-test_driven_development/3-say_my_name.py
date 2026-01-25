#!/usr/bin/python3

"""
This module defines a function to print a formatted name.
"""


def say_my_name(first_name, last_name=""):
    """Docstring for say_my_name

    Args:
        first_name: the first name
        last_name: the last name

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
        TypeError: If rows of the matrix have different sizes
        TypeError: If div is not a number
        ZeroDivisionError: If div is equal to 0
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
