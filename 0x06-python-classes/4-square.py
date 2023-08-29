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
        Initializes a new suqare instance

        Args:
            size (int):Size of one side of the square
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for size attribute

        Return:
            int: The size of one side of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size attribute

        Args:
            value (int): Size of one side of the square

        Raises:
            TypeError: If value is not an int
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of a square

        Return:
            int: Area of the square
        """
        return self.size ** 2
