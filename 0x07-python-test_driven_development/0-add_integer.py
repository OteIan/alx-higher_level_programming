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
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    
    return a + b