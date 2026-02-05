#!/usr/bin/python3

"""CountedIterator
Class that count the iteration of an object
"""


class CountedIterator:
    """
    Class that count the iteration of an object
    """
    def __init__(self, some_iterable):
        self._iterator = iter(some_iterable)
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self._iterator)
        self._count += 1
        return item

    def get_count(self):
        return self._count
