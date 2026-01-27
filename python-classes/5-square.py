#!/usr/bin/python3

class Square:
    """
    Class Square
    """
    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    def size(self, value: int):
        self.size = value

    def size(self: int) -> int:
        return self.size
    
    def area(self: int) -> int:
        if not isinstance(self.size, int):
            raise TypeError("size must be an integer")
        return self.size * self.size

    def my_print(self):
        if self.size == 0:
            print()
        else:
            print(("#" * self.size + "\n") * self.size, end="")
