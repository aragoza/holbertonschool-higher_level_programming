#!/usr/bin/python3
"""is_kind_of_class
a function that check for an object to be an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
    check for the same class type between an obj and a class
    """
    return isinstance(obj, a_class)
