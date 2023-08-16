#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    max_value = None
    for value in a_dictionary.values():
        if max_value is None or value > max_value:
            max_values = value
    return max_values
