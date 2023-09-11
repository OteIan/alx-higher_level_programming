#!/usr/bin/python3
""" Definition of MyInt subclass of Int class """


class MyInt(int):
    """ Rebel version of an int """
    def __new__(cls, *args, **kwargs):
        """ New class instance is created """
        return super(MyInt, cls).__new__(cls, *args, **kwargs)
    
    def __eq__(self, other):
        """ What was == is now != """
        return int(self) != other
    
    def __ne__(self, other):
        """ What was != is now == """
        return int(self) == other
