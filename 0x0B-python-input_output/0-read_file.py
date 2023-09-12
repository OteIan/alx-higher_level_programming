#!/usr/bin/python3
"""
This script defines a function 'read_file' that reads and prints the contents
of a text file.

Usage:
    To use this script, simply call the 'read_file' function with the
    filename as an argument.

Example:
    read_file("example.txt")
"""


def read_file(filename=""):
    """
    Read and print the contents of a text file.

    Parameters:
        filename (str): The name of the file to be read.

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
