#!/usr/bin/python3

def pow(a, b):
    a_origin = a
    for i in range(b-1):
        a = a * a_origin

    return a
