#!/usr/bin/python3
"""Checks if an object is an instance of a specified class."""


def is_same_class(obj, a_class):
    """Return True if the object is an instance of the specified class,
    otherwise return False.
    """
    return type(obj) == a_class
