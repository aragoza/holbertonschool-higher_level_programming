#!/usr/bin/python3

"""
function that verify for string in json
"""


import json


def save_to_json_file(my_obj, filename):
    """
    function that check for string in a json file

    parameter: my_str
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
