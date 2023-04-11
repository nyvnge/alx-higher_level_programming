#!/usr/bin/python3
"""Checking class function definition"""


def is_same_class(obj, a_class):
    """Check if object is an instance of the given class
    arguments:
        obj (any) - The object to check
        a_class (type) - class to match the type of object
    returns:
        If obj is an instance of a_class - 1
        Otherwise - 0
    """
    if type(obj) == a_class:
        return True
    return False
