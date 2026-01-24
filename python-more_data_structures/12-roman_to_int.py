#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string == "":
        return 0

    total = 0
    list_of_number = []
    dict_roman_int = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    for k in range(len(roman_string)):
        for i in dict_roman_int:
            if roman_string[k] == i:
                list_of_number.append(dict_roman_int[i])
    list_of_number.reverse()
    
    for i in range(len(list_of_number)):
        if  i < len(list_of_number) - 1 and list_of_number[i] > list_of_number[i + 1]:
            total -= list_of_number[i]
        else:
            total += list_of_number[i]


    return total
