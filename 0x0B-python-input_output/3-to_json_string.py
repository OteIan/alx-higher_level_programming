#!/usr/bin/python3
"""
This script defines a function 'to_json_string' that converts a Python object
to a JSON-formatted string

Usage:
    To use this script, call the 'to_json_string' function with a Python
    object as an argument

Example:
    my_dict = {"name": "John", "age": 30}
    json_string = to_json_string(my_dict)
"""


import json


def to_json_string(my_obj):
    """
    Convert a Python object to a JSON-formatted string.

    Parameters:
        my_obj: The Python object to be converted to JSON.

    Returns:
        str: A JSON-formatted string representation of the input object.
    """
    return json.dumps(my_obj)
