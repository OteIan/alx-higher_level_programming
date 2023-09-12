#!/usr/bin/python3
"""
This script defines a function 'load_from_json_file' that loads a Python object
from a JSON file

Usage:
    To use this script, call the 'load_from_json_file' function with a
    filename as an argument

Example:
    loaded_data = load_from_json_file("input.json")
"""


import json


def load_from_json_file(filename):
    """
    Load a Python object from a JSON file.

    Parameters:
        filename (str): The name of the JSON file from which the object will
        be loaded

    Returns:
        object: The Python object loaded from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
