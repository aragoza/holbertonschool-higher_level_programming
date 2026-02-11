#!/usr/bin/python3

"""
Docstring load, add and save
"""

import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    temp = load_from_json_file("add_item.json")
except (FileNotFoundError):
    temp = []

for i in sys.argv[1:]:
    temp.append(i)

save_to_json_file(temp, "add_item.json")
