#!/usr/bin/python3
"""read_file function"""


def read_file(filename=""):
    """reads a text file (UTF8) and outputs it to stdout"""

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end=""
