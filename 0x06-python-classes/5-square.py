#!/usr/bin/python3
"""Square class definition"""


class Square:
    """
    This defines a square based on the provided size

    Attributes:
        __size (int): Size of one side of the square (Private attribute)
    """
    def __init__(self, size=0):
        """
        Initializes a new square instance

        Args:
            size (int): Size of one side of the square
        """
        self.size = size

    @property
    def size(self):
        """
        Getter for the size attribute

        Return:
            int: Size of one side of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute

        Args:
            value (int): Size of one side of the square

        Raises:
            TypeError: If value is not an int
            ValueEror: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square

        Return:
            int: Area of the square
        """
        return self.size ** 2

    def my_print(self):
        """Prints the square with the character #"""
        if self.size == 0:
            print("")
        for i in range(self.size):
            for j in range(self.size):
                print('#', end='')
            print()
