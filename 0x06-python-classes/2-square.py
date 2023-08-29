#!/usr/bin/python3
"""Square class definiiton"""


class Square:
    """
    This class defines a square based on the provided size

    Arguments:
        __size (int): Size of on side of the square (Private attribute)
    """
    def __init__(self, size=0):
        """
        Initializes a new square instance

        Args:
            size (int, optional): Size of one side of the square (Default is 0)
                It must be a non negative integer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
