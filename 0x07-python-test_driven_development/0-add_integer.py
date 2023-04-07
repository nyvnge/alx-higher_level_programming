#!/usr/bin/python3
"""This is an integer addition function."""


def add_integer(x, y=98):
    """Returns integer addition of x & y
    Float arguments are typecasted to ints then addition is performed
    Raises:
        Typecast Error if x and b are not integers
    """
    if ((not isinstance(x, int) and not isinstance(a, float))):
        raise TypeError("x must be an integer")
    if ((not isinstance(y, int) and not isinstance(b, float))):
        raise TypeError("y must be an integer")
    return (int(x) + int(y))
