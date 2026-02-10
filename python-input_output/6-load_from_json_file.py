#!/usr/bin/python3

"""
function that verify for string in json
"""


import json


def load_from_json_file(filename):
    """
    function that check for string in a json file

    parameter: my_str
    """

    with open(filename, 'r', encoding="utf-8") as f:
        return json.loads(json.dumps(json.load(f)))
