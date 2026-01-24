#!/usr/bin/python3

def best_score(a_dictionary):
    
    if a_dictionary == None:
        return None

    b = "yes"    

    for key in a_dictionary:
        if a_dictionary[key] == None:
            continue
        if b == "yes":
            score = a_dictionary[key]
            b = "no"
        if score < a_dictionary[key]:
            score = a_dictionary[key]

    return score
