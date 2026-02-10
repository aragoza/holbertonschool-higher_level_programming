#!/usr/bin/python3

"""
function that verify for string in json
"""


import json


def from_json_string(my_str):
    """
    function that check for string in a json file

    parameter: my_str
    """

    return json.loads(my_str)
