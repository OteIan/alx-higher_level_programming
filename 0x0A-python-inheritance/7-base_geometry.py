#!/usr/bin/python3
""" BaseGeometry class definition """


class BaseGeometry:
    """  """
    def area(self):
        """ Raises an exceptiom """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """ This validates 'value' to make sure it is a positive int """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
