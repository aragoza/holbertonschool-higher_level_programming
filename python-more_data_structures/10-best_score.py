#!/usr/bin/python3

def best_score(a_dictionary):
    
    if a_dictionary == None:
        return None

    b = "yes"    

    for key in a_dictionary:
        if b == "yes":
            best_key = key
            b = "no"
            continue
        if a_dictionary[best_key] < a_dictionary[key]:
            best_key = key

    return best_key
