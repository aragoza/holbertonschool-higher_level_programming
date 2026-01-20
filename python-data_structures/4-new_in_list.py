#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    new_list = []
    if idx not in range(len(my_list)):
        return my_list
    elif idx in range(len(my_list)):
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
