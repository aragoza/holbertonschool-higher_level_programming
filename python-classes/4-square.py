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
    



my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)