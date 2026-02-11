#!/usr/bin/python3

"""
serialize and deserialize
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    Docstring for serialize_and_save_to_file

    :param data: Description
    :param filename: Description
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Docstring for load_and_deserialize

    :param filename: Description
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
