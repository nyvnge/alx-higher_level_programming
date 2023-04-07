#!/usr/bin/python3
"""This defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Print a name
    Args:
        first_name (str): first name to print.
        last_name (str): last name to print.
    Raises:
        TypeError If first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("firstname must be a string")
    if not isinstance(last_name, str):
        raise TypeError("lastname must be a string")
    print("My name is {} {}".format(first_name, last_name))
