#!/usr/bin/python3
"""inherits_from function."""


def inherits_from(obj, a_class):
    """If object is an inherited instance of a_class - True. Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
