#!/usr/bin/python3
"""read_file function"""


def read_file(filename=""):
    """reads a text file (UTF8) and outputs it to stdout"""

    with open(filename, "r", encoding="utf-8") as x:
        print(x.read(), end="")
