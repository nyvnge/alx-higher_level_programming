#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an obj is an instance//inherited instance of a class.

    arguments:
        obj (any): The object to check
        a_class (type): The class to match the type of obj to
    returns:
        bool: If obj is an instance or inherited instance of a_class - True, 
        otherwise - False
    """
    if isinstance(obj, a_class):
        return True
    return False
