#!/usr/bin/python3

def common_elements(set_1, set_2):
    list_common_element = []
    for i in set_1:
        if i in set_2:
            list_common_element.append(i)

    return list_common_element
