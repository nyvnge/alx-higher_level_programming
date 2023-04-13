#!/usr/bin/python3
"""
append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """appends "new_string" after a line """
    with open(filename, 'r', encoding='utf-8') as x:
        line_list = []
        while True:
            line = x.readline()
            if line == "":
                break
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)
    with open(filename, 'w', encoding='utf-8') as x:
        x.writelines(line_list)
