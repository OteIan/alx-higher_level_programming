#!/usr/bin/python3
"""
"""
from models.base import Base


class Rectangle(Base):
    """  """
    def __init__(self, width, height, x=0, y=0, id=None):
        """  """
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
        """  """
        return self.__width

    @width.setter
    def width(self, value):
        """  """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # Validate Height
    @property
    def height(self):
        """  """
        return self.__height

    @height.setter
    def height(self, value):
        """  """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # Validate x
    @property
    def x(self):
        """  """
        return self.__x

    @x.setter
    def x(self, value):
        """  """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # Validate y
    @property
    def y(self):
        """  """
        return self.__y

    @y.setter
    def y(self, value):
        """  """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """  """
        return self.__height * self.__width

    def display(self):
        """  """
        for _ in range(self.__y):
            print()
        for i in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """  """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """  """
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
        """  """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
