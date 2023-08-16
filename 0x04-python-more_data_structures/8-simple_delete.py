#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary.__contains__(key) is True:
        a_dictionary.__delitem__(key)
    return a_dictionary
