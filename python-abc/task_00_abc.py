#!/usr/bin/python3

"""
Docstring for holbertonschool-higher_level_programming.python-abc.task_00_abc
"""


from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Docstring for Animal
    """

    @abstractmethod
    def sound(self):
        ...


class Dog(Animal):
    """
    Docstring for Dog
    """

    def sound(self):
        return "Bark"

class Cat(Animal):
    """
    Docstring for Cat
    """

    def sound(self):
        return "Meow"
