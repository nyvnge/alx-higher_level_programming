#!/usr/bin/python3
"""This is an integer addition function."""


def add_integer(a, b=98):
    """Returns integer addition of a & b
    Float arguments are typecasted to ints then addition is performed
    Raises:
        Typecast Error if a and b are not integers
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
