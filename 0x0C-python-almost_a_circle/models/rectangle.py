#!/usr/bin/python3
"""
This module defines a 'Rectangle' class that represents rectangles and
inherits properties from the 'Base' class.

Usage:
    To use this module, create instances of the 'Rectangle' class, providing
    width, height, and optional position (x, y) and ID.

Example:
    r = Rectangle(10, 5, 2, 3, 1)
    print(r.area())  # Outputs the area of the rectangle (50)
    r.display()     # Displays the rectangle
    print(r)         # Outputs the string representation of the rectangle
    r.update(2, 8, 4, 1, 6)  # Updates the rectangle attributes
    r_dict = r.to_dictionary()  # Converts the rectangle to a dictionary
"""
from models.base import Base


class Rectangle(Base):
    """
    A class for representing rectangles.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the top-left corner of the rectangle.
        y (int): The y-coordinate of the top-left corner of the rectangle.
        id (int): The ID of the rectangle.

    Inherits Attributes:
        id (int): The ID of the rectangle (inherited from the 'Base' class).
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the top-left corner of the
                                rectangle.
            y (int, optional): The y-coordinate of the top-left corner of the
                                rectangle.
            id (int, optional): The ID of the rectangle. If not provided, a
                                unique ID will be generated.

        Raises:
            TypeError: If any of the arguments are not integers.
            ValueError: If width or height is less than or equal to 0, or if
                        x or y is less than 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id

        # inheriting properties of the parent class
        super().__init__(id)

    # Validate Width
    @property
    def width(self):
        """ Get or set the width of the rectangle as an integer. """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # Validate Height
    @property
    def height(self):
        """ Get or set the height of the rectangle as an integer. """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # Validate x
    @property
    def x(self):
        """ Get or set the x-coordinate of the top-left corner of the rectangle
        as an integer. """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the top-left corner of the rectangle.

        Args:
            value (int): The x-coordinate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # Validate y
    @property
    def y(self):
        """ Get or set the y-coordinate of the top-left corner of the rectangle
        as an integer. """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the top-left corner of the rectangle.

        Args:
            value (int): The y-coordinate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width

    def display(self):
        """ Display the rectangle using '#' characters. """
        for _ in range(self.__y):
            print()
        for i in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string in the format '[Rectangle] (id) x/y - width/height'.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle.

        Args:
            *args: Variable length argument list. If provided, updates in the
                    order (ID, Width, Height, X, Y).
            **kwargs: Arbitrary keyword arguments for attribute updates.

        Note:
            If both args and kwargs are provided, args take precedence over
            kwargs.

        Example:
            r.update(2, 8, 4, 1, 6)  # Updates the rectangle attributes.
        """
        if args is None or len(args) == 0:
            for key, value in kwargs.items():
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value
                if key == "id":
                    self.id = value

        argc = len(args)
        if argc >= 1:
            self.id = args[0]
        if argc >= 2:
            self.__width = args[1]
        if argc >= 3:
            self.__height = args[2]
        if argc >= 4:
            self.__x = args[3]
        if argc >= 5:
            self.__y = args[4]

    def to_dictionary(self):
        """
        Convert the rectangle attributes to a dictionary.

        Returns:
            dict: A dictionary containing 'id', 'width', 'height', 'x', and 'y'
                    keys.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
