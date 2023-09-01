#!/usr/bin/python3
""" This defines a function that prints the given name input """


def say_my_name(first_name, last_name=""):
    """
    
    """
    if first_name is None:
        return None
    if isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")