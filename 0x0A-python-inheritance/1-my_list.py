#!/usr/bin/python3
""" Class MyList Definition """


class MyList(list):
    """ This inherits from list """
    def print_sorted(self):
        """ Prints a sorted version of a list in ascending order """
        sorted_list = sorted(self)
        print(sorted_list)