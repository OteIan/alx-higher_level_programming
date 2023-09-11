#!/usr/bin/python3
""" This module contains 'is_kind_of_class' function """


def is_kind_of_class(obj, a_class):
    """
    This checks if an object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class

    Args:
        obj: Object to be compared
        a_class: Object to be compared against

    Return:
        True if object is an instance of, or an instance of a subclass of, the
        specified class, otherwise False
    """
    return isinstance(obj, a_class)
