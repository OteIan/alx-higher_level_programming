#!/usr/bin/python3
""" Locked class definition """


class LockedClass:
    """
    Prevents the user from instantiating new LockedClass attributes
    for anything but attributes for 'first_name'
    """
    __slots__ = ["first_name"]
    