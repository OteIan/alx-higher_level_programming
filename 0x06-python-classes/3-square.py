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
        This initializes a new square instance

        Args:
            size (int, optional): Size of one side of the square (Default is 0)
                It must be a non negative number
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        This calculates the area of the square

        Return: 
            int: Current square area
        """
        return self.__size ** 2
