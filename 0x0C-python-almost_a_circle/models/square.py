#!/usr/bin/python3
"""
This module defines a 'Square' class that represents squares and
inherits properties from the 'Rectangle' class.

Usage:
    To use this module, create instances of the 'Square' class, providing
    size, and optional position (x, y) and ID.

Example:
    r = Square(5, 2, 3, 1)
    print(r.area())  # Outputs the area of the rectangle (25)
    r.display()     # Displays the square
    print(r)         # Outputs the string representation of the square
    r.update(2, 4, 1, 6)  # Updates the square attributes
    r_dict = r.to_dictionary()  # Converts the square to a dictionary
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class for representing squares.

    Attributes:
        size (int): The size of one side of the square.

    Inherits Attributes:
        id (int): The id of the square.
        x (int): The x-coordinate of the top-left corner of the square.
        y (int): The y-coordinate of the top-left corner of the square.
        id (int): The id of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square object.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the top-left corner.
            y (int): The y-coordinate of the top-left corner.
            id (int, optional): An optional ID for the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Get or set the size of the square. """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments for attribute updates.

        Note:
            If both args and kwargs are provided, args take precedence over
            kwargs.

        Example:
            square.update(2, 8, 4, 2)  # Updates the square attributes.
        """
        if args is not None or len(args) == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
        argc = len(args)
        if argc >= 1:
            self.id = args[0]
        if argc >= 2:
            self.size = args[1]
        if argc >= 3:
            self.x = args[2]
        if argc >= 4:
            self.y = args[3]

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string in the format '[Square] (id) x/y - size'.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def to_dictionary(self):
        """
        Convert the square attributes to a dictionary.

        Returns:
            dict: A dictionary containing 'id', 'size', 'x', and 'y' keys.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
