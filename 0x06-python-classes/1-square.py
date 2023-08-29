#!/usr/bin/python3
"""Square class definition"""


class Square:
    """
    This class defines a suqare based on the provided size

    Attributes:
        __size (int): Size of a side of a square
    """
    def __init__(self, size):
        """
        Initializes a new Square instance

        Args:
            size (int): Size of the square
        """
        self.__size = size
