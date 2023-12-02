#!/usr/bin/python3
"""Method for finding the peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """ Finds the peak in a list of unsorted integers"""
    if list_of_integers == []:
        return None
    return max(list_of_integers)
