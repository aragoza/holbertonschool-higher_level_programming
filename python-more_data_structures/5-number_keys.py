#!/usr/bin/python3

def number_keys(a_dictionary):
    count = 0
    for i in a_dictionary:
        if a_dictionary.get(a_dictionary[i], False) == False:
            count += 1

    return count
