#!/usr/bin/python3

"""
class Verboselist inherits of list so of its method
"""


class VerboseList(list):
    """
    Class VerboseList
    """

    def append(self, object):
        """
        Docstring for append

        :param self: Description
        :param object: Description
        """
        super().append(object)
        print("Added [{}] to the list.".format(object))

    def extend(self, iterable):
        """
        Docstring for extend

        :param self: Description
        :param iterable: Description
        """
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, value):
        """
        Docstring for remove

        :param self: Description
        :param value: Description
        """
        print("Removed [{}] from the list.".format(value))
        super().remove(value)

    def pop(self, index=-1):
        """
        Docstring for pop

        :param self: Description
        :param index: Description
        """
        print("Popped [{:d}] from the list.".format(self[index]))
        super().pop(index)
