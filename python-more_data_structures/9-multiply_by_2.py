#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for i in a_dictionary:
        new_dict[i] = 2*a_dictionary[i]

    return new_dict
