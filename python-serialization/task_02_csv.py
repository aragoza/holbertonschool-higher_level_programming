#!/usr/bin/python3

"""
Docstring for task_02_csv
"""

import json
import csv


def convert_csv_to_json(filename):
    """
    Docstring for convert_csv_to_json

    :param filename: Description
    """
    row = []

    try:
        with open(filename, 'r', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for i in reader:
                row.append(i)

        with open('data.json', 'w', encoding="utf-8") as f:
            json.dump(row, f)

        return True

    except FileNotFoundError:
        return False
