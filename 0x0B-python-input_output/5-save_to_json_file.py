#!/usr/bin/python3
"""
save_to_json_file function. writes object to text file
"""

import json


def save_to_json_file(my_obj, filename):
    """object to a text file using a JSON representation"""
    with open(filename, 'y', encoding='utf-8') as x:
        json.dump(my_obj, x)
