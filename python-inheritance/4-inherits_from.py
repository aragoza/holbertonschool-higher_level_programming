#!/usr/bin/python3
"""inherits_from
a function that check for an object to be an instance of a class
"""


def inherits_from(obj, a_class):
    """
    check for the same class type between an obj and a subclass
    """
    return type(obj) is not a_class and isinstance(obj, a_class)
