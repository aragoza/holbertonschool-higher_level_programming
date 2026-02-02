#!/usr/bin/python3
"""is_same_class
a function that check for an object to be an instance of a class
"""


def is_same_class(obj, a_class):
    """
    check for the same class type between an obj and a class
    """
    return type(obj) is a_class
