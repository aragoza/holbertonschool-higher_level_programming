#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    list_common_element = []
    for i in set_1:
        if i not in set_2:
            list_common_element.append(i)
    for i in set_2:
        if i not in set_1:
            list_common_element.append(i)

    return list_common_element
