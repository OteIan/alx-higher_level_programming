#!/usr/bin/python3
""" Rectangle subclass definition """


class BaseGeometry:
    """
    BaseGeometry is a base class for representing geometric shapes and
    performing related operations.

    Methods:
    - area(self): Placeholder method for calculating the area of a geometric
    shape. Subclasses should override this method with their own
    implementations

    - integer_validator(self, name, value): Validates that a given value
    is a positive integer.

    Attributes:
    None

    Usage:
    This class is intended to be subclassed to create specific geometric
    shape classes.
    """

    def area(self):
        """
        Placeholder method for calculating the area of a geometric shape.
        Subclasses should override this method with their own implementations.

        Raises:
        Exception: This method raises an Exception with the message
        "area() is not implemented."

        Returns:
        None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a given value is a positive integer.

        Args:
        name (str): A string representing the name of the value being validated
        value (int): The value to be validated.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is not greater than 0.

        Returns:
        None
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Rectangle is a class that represents a geometric rectangle and inherits from BaseGeometry.

    Attributes:
    - __width (int): The width of the rectangle.
    - __height (int): The height of the rectangle.

    Methods:
    - __init__(self, width, height): Initializes a new rectangle
    instance based on the given width and height.
    """
    def __init__(self, width, height):
        """
        This initializes a new rectangle instance based on the given
        width and height

        Args:
            __width (int): width of the rectangle
            __height (int): height of the rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
