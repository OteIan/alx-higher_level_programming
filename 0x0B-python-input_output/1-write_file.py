#!/usr/bin/python3
"""
This script defines a function 'write_file' that writes text to a specified
file

Usage:
    To use this script, call the 'write_file' function with the filename
    and text as arguments

Example:
    write_file("example.txt", "Hello, World!")
"""


def write_file(filename="", text=""):
    """
    Write text to a specified file.

    Parameters:
        filename (str): The name of the file to which text will be written.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
