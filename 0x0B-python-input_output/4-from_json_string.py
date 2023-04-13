#!/usr/bin/python3
"""
from_json_string function
"""

import json


def from_json_string(my_str):
    """returns an object represented by JSON string"""
    return json.loads(my_str)
