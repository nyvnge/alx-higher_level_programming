#!/usr/bin/python3
"""This defines text-indentation function."""


def text_indentation(text):
    """Output text with new lines after '.', '?', and ':'
    args:
       param text (string): text to print.
    Raises:
        TypeError: If text isn't string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    x = 0
    while x < len(text) and text[x] == ' ':
        x += 1

    while x < len(text):
        print(text[x], end="")
        if text[x] == "\n" or text[x] in ".?:":
            if text[x] in ".?:":
                print("\n")
            x += 1
            while x < len(text) and text[x] == ' ':
                x += 1
            continue
        x += 1
