#!/usr/bin/python3
"""Method for finding the peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """ Finds the peak in a list of unsorted integers"""
    if list_of_integers == []:
        return None
    
    length = len(list_of_integers)
    i = int(length / 2)
    li = list_of_integers
    
    if i - 1 < 0 and i + 1 >= length:
        return li[i]
    elif i - 1 < 0:
        if li[i] > li[i + 1]:
            return li[i]
        return li[i + 1]
    elif i + 1 >= length:
        if li[i] > li[i - 1]:
            return li[i]
        return li[i - 1]
    
    if li[i - 1] < li[i] > li[i + 1]:
        return li[i]
    
    if li[i + 1] > li[i - 1]:
        return find_peak(li[i:])
    return find_peak(li[:i])