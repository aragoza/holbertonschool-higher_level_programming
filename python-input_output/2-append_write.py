#!/usr/bin/python3

"""
Docstring
"""


import sys


def append_write(filename="", text=""):
    """
    Docstring for append_write
    
    :param filename: Description
    :param text: Description
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
