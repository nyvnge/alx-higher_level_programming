#!/usr/bin/python3
"""
load_from_json_file function. creates object from JSON file
"""

import json


def load_from_json_file(filename):
    """crate and object from JSON file """
    with open(filename, 'r', encoding='utf-8') as x:
        return json.load(x)
