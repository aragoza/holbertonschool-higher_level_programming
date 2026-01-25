#!/usr/bin/python3

def add_integer(a, b=98):
    """Add two integers

    Args:
        a : first number
        b : second number

    Raises:
        TypeError: if a or b is not an integer or float
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
