#!/usr/bin/python3
"""add load & save a add_item ""JSON file"" """

import sys


if __name__ == "__main__":

    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file

    try:
        x_items = load("add_item.json")
    except FileNotFoundError:
        x_items = []

    x_items.extend(sys.argv[1:])
    save(x_items, "add_item.json")
