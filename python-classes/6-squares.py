#!/usr/bin/python3

class Square:
    """
    Class Square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self: int) -> int:
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        return self.__size

    @size.setter
    def size(self, value: int):
        self.__size = value
    
    def area(self: int) -> int:
        if not isinstance(self.size, int):
            raise TypeError("size must be an integer")
        return self.__size * self.__size

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
