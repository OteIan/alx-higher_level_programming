#!/usr/bin/python3
""" Rectangle subclass definition """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle is a class that represents a geometric rectangle and inherits
    from BaseGeometry.

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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle and returns it

        Return:
            int: Area of the rectangle
        """
        return self.__width * self.__height
    
    def __str__(self):
        """ Informal string representation of a rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
