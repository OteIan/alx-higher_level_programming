#!/usr/bin/python3
"""
This script defines a function 'append_write' that appends text to a
specified file

Usage:
    To use this script, call the 'append_write' function with the
    filename and text as arguments.

Example:
    append_write("example.txt", "Additional text to append.")
"""


def append_write(filename="", text=""):
    """
    Append text to a specified file.

    Parameters:
        filename (str): The name of the file to which text will be appended.
        text (str): The text to be appended to the file.

    Returns:
        int: The number of characters appended to the file.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))
