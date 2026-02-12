#!/usr/bin/python3

"""
Docstring for task_01_pickle
"""

import pickle


class CustomObject:
    """
    Docstring for CustomObject
    """

    def __init__(self, name, age, is_student):
        """
        Docstring for __init__

        :param self: Description
        :param name: Description
        :param age: Description
        :param is_student: Description
        """
        self.age = age
        self.name = name
        self.is_student = is_student

    def display(self):
        """
        Docstring for display

        :param self: Description
        """
        a = self.age
        n = self.name
        i = self.is_student
        print("Name: {}\nAge: {}\nIs Student: {}".format(a, n, i))

    def serialize(self, filename):
        """
        Docstring for serialize

        :param self: Description
        :param filename: Description
        """
        if filename is None or self is None:
            return None
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """
        Docstring for deserialize

        :param cls: Description
        :param filename: Description
        """
        if filename is None or cls is None:
            return None
        with open(filename, 'rb') as f:
            return pickle.load(f)
