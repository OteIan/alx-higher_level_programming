#!/usr/bin/python3
""" Print square function definition """


def print_square(size):
    """
    Prints a square depending on the given size with the character '#'

    Args:
        size (int): Size length of a square

    Raises:
        TypeError: If 'size' is not an integer
        ValueError: If 'size' is less than 0
    """
    if ((isinstance(size, float) and size < 0) or
        not isinstance(size, int)):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")