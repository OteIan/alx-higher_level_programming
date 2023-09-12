#!/usr/bin/python3
"""
This script defines a function 'save_to_json_file' that saves a Python object
to a JSON file

Usage:
    To use this script, call the 'save_to_json_file' function with a Python
    object and a filename as arguments

Example:
    my_dict = {"name": "John", "age": 30}
    save_to_json_file(my_dict, "output.json")
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Save a Python object to a JSON file.

    Parameters:
        my_obj: The Python object to be saved.
        filename (str): The name of the JSON file to which the object will be
        saved

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
