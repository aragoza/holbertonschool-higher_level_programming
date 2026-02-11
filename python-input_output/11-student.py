#!/usr/bin/python3

"""
Docstring
"""

class Student:
    """
    Docstring for Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Docstring for __init__

        :param self: Description
        :param first_name: Description
        :param last_name: Description
        :param age: Description
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Docstring for to_json

        :param self: Description
        :param attrs: Description
        """
        dictionnary = dict()

        if attrs is None:
            for i in reversed(self.__dict__):
                dictionnary[i] = self.__dict__[i]
            return dictionnary

        for k in reversed(self.__dict__):
            if k in attrs:
                dictionnary[k] = self.__dict__[k]

        return dictionnary

    def reload_from_json(self, json):
        """
        Public method def reload_from_json(self, json): that replaces all attributes of the Student instance
        
        :param self: Description
        :param json: Description
        """

        for k, v in json.items():
            setattr(self, k, v)
