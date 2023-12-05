#!/usr/bin/python3
"""
    The module returns a list of available attributes of an object
"""


def lookup(obj):
    """This functions looks up all attributes of an object"""
    return dir(obj)
