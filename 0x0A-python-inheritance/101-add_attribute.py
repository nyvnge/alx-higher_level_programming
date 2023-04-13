#!/usr/bin/python3
"""add_attributes function"""


def add_attribute(objct, attr, value):
    """Add a new attribute to an object if possible.
    """
    if not hasattr(objct, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(objct, attr, value)
