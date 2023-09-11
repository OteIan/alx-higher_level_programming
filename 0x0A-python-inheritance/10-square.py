#!/usr/bin/python3
"""
Definition of Square subclass of Rectangle subclass of BaseGeometry class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square is a subclass of Rectangle, which is in turn a subclass of the
    BaseGeometry class.
    It represents a geometric square.

    Attributes:
    - size (int): The side length of the square.

    Methods:
    - __init__(self, size): Initializes a new square instance based on the
    given side length.

    Notes:
    The Square class inherits from Rectangle and BaseGeometry, which
    provide the functionality
    for validation and area calculation.
    """
    def __init__(self, size):
        """
        Initializes a new square instance based on the given side length.

        Args:
        - size (int): The side length of the square.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is not greater than 0.

        Returns:
        None
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
