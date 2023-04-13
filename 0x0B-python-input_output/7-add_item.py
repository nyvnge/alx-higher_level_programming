#!/usr/bin/python3
"""
Add and save a add_item.json file
"""

from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

x = "add_item.json"

try:
    json_list = load_from_json_file(x)
except FileNotFoundError:
    json_list = []

for arg in argv[1:]:
    json_list.append(arg)

save_to_json_file(json_list, x)
