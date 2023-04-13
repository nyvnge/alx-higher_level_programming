#!/usr/bin/python3
"""
append_write function
"""


def append_write(filename="", text=""):
    """return the no of characters added"""
    with open(filename, 'a', encoding='utf=8') as x:
        return x.write(text)
