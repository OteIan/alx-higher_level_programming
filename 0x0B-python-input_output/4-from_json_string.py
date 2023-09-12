#!/usr/bin/python3
"""
This script defines a function 'from_json_string' that converts a
JSON-formatted string to a Python object

Usage:
    To use this script, call the 'from_json_string' function with a
    JSON-formatted string as an argument

Example:
    json_string = '{"name": "John", "age": 30}'
    my_dict = from_json_string(json_string)
"""


import json


def from_json_string(my_str):
    """
    Convert a JSON-formatted string to a Python object.

    Parameters:
        my_str (str): The JSON-formatted string to be converted.

    Returns:
        object: A Python object representation of the JSON input.
    """
    return json.loads(my_str)
