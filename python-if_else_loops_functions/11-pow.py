#!/usr/bin/python3

def pow(a, b):
    a_origin = a
    if b < 0:
        for i in range(-(b-1)):
            a = 1 / (a * a_origin)
    elif b == 0:
        return 1
    else:
        for i in range(b-1):
            a = a * a_origin
    return a
