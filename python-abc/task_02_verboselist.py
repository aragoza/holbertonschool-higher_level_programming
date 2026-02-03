#!/usr/bin/python3

"""
class Verboselist inherits of list so of its method
"""


class VerboseList(list):
    """
    Class VerboseList
    """

    def append(self, object):
        print("Added [{}] to the list.".format(object))
        return super().append(object)


    def extend(self, iterable):
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))



    def remove(self, value):        
        super().remove(value)
        print("Removed [{}] from the list.".format(value))


    def pop(self, index=-1):
        old_element = self[index]
        super().pop(index)
        print("Popped [{}] from the list.".format(old_element))
