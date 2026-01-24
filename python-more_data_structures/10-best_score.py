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


a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))