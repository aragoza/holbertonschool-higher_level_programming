#!/usr/bin/python3

"""
Docstring
"""


def read_file(filename=""):
    """
    Docstring for read_file
    
    :param filename: Description
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read())
