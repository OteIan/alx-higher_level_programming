#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for element in a_dictionary:
        if key == element:
            a_dictionary.__setitem__(element, value)
    a_dictionary[key] = value
    return a_dictionary
