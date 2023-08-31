#!/usr/bin/python3
"""Square class definition"""


class Square:
    """
    This defines a square based on the provided value and position

    Attributes:
        __size (int): Size of one side of the square
        __position (tuple): Position of the square
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
            TypeError: If is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
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
            return
        for a in range(self.position[1]):
            print("")
        for i in range(self.size):
            for b in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print("")

        def __str__(self):
            """Define the print() representation of a square"""
            if self.__size == 0:
                return ""

            output = ""
            for _ in range(self.position[1]):
                output += "\n"

            for _ in range(self.size):
                output += " " * self.position[0]
                output += "#" * self.size
                output += "\n"

            return output
