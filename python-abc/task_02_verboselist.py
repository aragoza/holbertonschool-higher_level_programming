#!/usr/bin/python3

"""
class Verboselist inherits of list so of its method
"""


class VerboseList(list):
    """
    Class VerboseList
    """

class VerboseList(list):
    """
    Class VerboseList
    """

    def append(self, item):
        """
        Docstring for append
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """
        Docstring for extend
        """
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, value):
        """
        Docstring for remove
        """
        print("Removed [{}] from the list.".format(value))
        super().remove(value)

    def pop(self, index=-1):
        """
        Docstring for pop
        """
        item = self[index]
        result = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return result
