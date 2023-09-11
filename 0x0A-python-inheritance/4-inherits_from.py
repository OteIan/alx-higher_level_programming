#!/usr/bin/python3
""" This module has 'inherits_from' function """


def inherits_from(obj, a_class):
    """
    This checks if object has been inherited from a_class

    Args:
        obj: Object to be compared
        a_class: Object to be compared against

    Return: True if object is inherited from a_class otherwise False
    """
    return (type(obj) == a_class)
