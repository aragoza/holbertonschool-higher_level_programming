#!/usr/bin/python3
"""
MyList is a subclass from list that inherites of her
"""


class MyList(list):
    """
    MyList is a class that have a sorted list
    """

    def print_sorted(self):
        print(sorted(self))
