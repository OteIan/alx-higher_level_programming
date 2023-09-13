#!/usr/bin/python3
"""
This script defines a function 'class_to_json' that converts the attributes
of a class object to a JSON-compatible dictionary

Usage:
    To use this script, call the 'class_to_json' function with a class object
    as an argument

Example:
    class MyClass:
        def __init__(self):
            self.name = "John"
            self.age = 30

    my_instance = MyClass()
    json_data = class_to_json(my_instance)
"""


def class_to_json(obj):
    """
    Convert the attributes of a class object to a JSON-compatible dictionary.

    Parameters:
        obj: The class object to be converted to a dictionary.

    Returns:
        dict: A dictionary containing the attributes of the class object.

    Note:
        Only attributes of type list, dict, str, int, and bool are included
        in the dictionary
    """
    data = {}

    for name in dir(obj):
        if not name.startswith("__"):
            value = getattr(obj, name)
            if isinstance(value, (list, dict, str, int, bool)):
                data[name] = value

    return data
