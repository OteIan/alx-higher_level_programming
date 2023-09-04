#!/usr/bin/python3
""" Rectangle class definition """


class Rectangle:
    """
    This defines a rectangle based on the provided width and height

    Attributes:
        __width (int): Width of the rectangle
        __height (int): Height of the rectangle
        number_of_instances (int): Number of instances created
        print_symbol (str): Symbol used to print the rectangle
    """
    number_of_instances = 0  # Class-level attribute to count instances
    print_symbol = "#"  # Class-level attribute to define the print symbol

    def __init__(self, width=0, height=0):
        """
        This initializes a new rectangle instance

        Args:
            width (int): Width of the rectangle (Default is 0)
            height (int): Height of the rectangle (Default is 0)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """
        Returns a string representation of the rectangle using print_symbol

        Returns:
            str: String representation of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return ""

        rectangle_str = ""
        for i in range(self.height):
            rectangle_str += str(self.print_symbol) * self.width + '\n'
        return rectangle_str.strip()

    def __repr__(self):
        """
        Returns a string representation of the rectangle for recreation

        Return:
            str: String representation of the rectangle
        """
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        """
        Destructor method for Rectangle instance

        It prints a farewell message and decrements the number_of_instances
        attributes
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares the area of two rectangles and returns the larger one

        Args:
            rect_1 (Rectangle): First rectangle
            rect_2 (Rectangle): Second rectangle

        Raises:
            TypeError: If either 'rect_1' or 'rect_2' is not an instance of
            Rectangle

        Return:
            int: Area of the larger rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a square with the given size

        Args:
            size (int): Size of the square rectangle. (Default is 0)

        Returns:
            Rectangle: A square with the given size
        """
        return cls(size, size)
