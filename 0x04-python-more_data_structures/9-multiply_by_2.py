#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for element in new_dict:
        new_dict[element] *= 2
    return new_dict
