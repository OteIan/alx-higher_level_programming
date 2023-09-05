#!/usr/bin/python3
"""Addition of integers definition"""


def add_integer(a, b=98):
    """
    This adds two integers and returns the total

    Args:
        a (int): First integer
        b (int): Second integer (Default is 98)

    Return:
        int: Sum of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)