#!/usr/bin/python3
"""This defines square-printing function."""


def print_square(size):
    """Output a square with the # character
    Args:
        param (int): The height/width of the square.
    Raises:
        TypeError: If size isn't an integer
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an int")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        [print("#", end="") for y in range(size)]
        print("")
