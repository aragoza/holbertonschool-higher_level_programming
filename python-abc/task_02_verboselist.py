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

    def pop(self, index=-1):
        """
        Docstring for pop

        :param self: Description
        :param index: Description
        """
        old_element = self[index]
        super().pop(index)
        print("Popped [{}] from the list.".format(old_element))
