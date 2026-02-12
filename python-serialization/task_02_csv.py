#!/usr/bin/python3

"""
Docstring for task_02_csv
"""

import json, csv

def convert_csv_to_json(filename):
    """
    Docstring for convert_csv_to_json
    
    :param filename: Description
    """
    row = []

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for i in reader:
            row.append(i)
    
    with open('data.json', 'w', ) as f:
        json.dump(row, f)
