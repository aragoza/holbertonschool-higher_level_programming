#!/usr/bin/python3

"""
Docstring for holbertonschool-higher_level_programming.python-input_output.0-read_file
"""


import sys


def read_file(filename=""):
    """
    Docstring for read_file
    
    :param filename: Description
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read())
