#!/usr/bin/python3
""" This defines a function that prints the given name input """


def say_my_name(first_name, last_name=""):
    """
    This prints out a name based on the given inputs

    Args:
        first_name (str): The first name
        last_name (str) The last name

    Raises:
        TypeError: If either names are not strings
    """
    if first_name == "":
        return ""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")