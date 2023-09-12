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
    """  """
    with open(filename, 'r') as file:
        json.load(filename)
