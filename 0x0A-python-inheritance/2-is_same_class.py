#!/usr/bin/python3
""" Function that compares 2 instances """


def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a specified class

    Args:
        obj: Object to be compared
        a_class: Class to be compared against

    Return:
        True if they are both an instance of specified class otherwise false
    """
    return (type(obj) == a_class)
