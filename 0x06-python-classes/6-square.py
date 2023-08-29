#!/usr/bin/python3
"""Square class definition"""


class Square:
    """
    This defines a square based on the given size and position

    Attributes:
        __size (int): Size of one side of the square (Private attribute)
        __position (tuple): Position of the square (Private attribute)
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        This initializes a new square instance

        Args:
            size (int, optional): Size of one side of the square
            position (tuple, optional): Position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for size attribute

        Return:
            int: Size of one side of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size attribute

        Args:
            value: Size of one side of the square

        Raises:
            TypeError: If value is not an int
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for position attribute

        Return:
            tuple: Position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for position attribute

        Args:
            value: Position of the square

        Raises:
            TypeError: If the tple has an int less than 0
        """
        if len(value) != 2 or not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in range(len(value)):
            if not isinstance(value[i], int) or value[i] < 0:
                raise TypeError("position must be a tuple of 2 positive\
                        integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square

        Return:
            int: Area of the square
        """
        return self.size ** 2

    def my_print(self):
        """Prints the area of the square in #"""
        if self.size == 0:
            print("")
        for a in range(self.position[1]):
            print("")
        for i in range(self.size):
            for b in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print("")
