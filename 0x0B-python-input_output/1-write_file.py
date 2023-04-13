#!/usr/bin/python3
"""
Write File function
"""


def write_file(filename="", text=""):
    """returns the number of chars written"""
    with open(filename, 'w', encoding='utf=8') as x:
        return x.write(text)
