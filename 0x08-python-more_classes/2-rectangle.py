#!/usr/bin/python3
""" Rectangle class definition """


class Rectangle:
    """
    This defines a rectangle based on the provided width and height

    Attributes:
        __width (int): Width of the rectangle
        __height (int): Height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        This initializes a new rectangle instance

        Args:
            width (int): Width of the rectangle (Default is 0)
            height (int): Height of the rectangle (Default is 0)
        """
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """
        Getter method for width attribute

        Return:
            int: Width of the rectangle
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        Setter method for width attribute

        Args:
            value (int): Width of the rectangle

        Raises:
            TypeError: If 'value' is not an integer
            ValueError: If 'value' is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height atttribute

        Return:
            int: Height of the rectangle
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        Setter method for height attribute

        Args:
            value (int): Height of the rectangle
        
        Raises:
            TypeError: If 'value' is not an integer
            ValueError: If 'value' is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle and returns the value

        Return:
            int: Area of the rectangle
        """
        return (self.__width * self.__height)
        
    def perimeter(self):
        """
        Calculates the perimeter of the rectangle and returns the value

        Return:
            int: Perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))