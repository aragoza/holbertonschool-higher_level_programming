#!/usr/bin/python3

"""
Docstring for python to xml
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Docstring for serialize_to_xml

    :param dictionary: Description
    :param filename: Description
    """
    root = ET.Element("data")

    for k, v in dictionary.items():
        element = ET.SubElement(root, k)
        element.text = str(v)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Docstring for deserialize_from_xml

    :param filename: Description
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}

    for element in root:
        result[element.tag] = element.text

    return result
