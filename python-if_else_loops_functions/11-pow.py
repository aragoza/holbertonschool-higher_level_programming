#!/usr/bin/python3

def pow(a, b):
    a_origin = a
    b_origin = b
    if b < 0:
        b = -b
    for i in range(b - 1):
        a = a * a_origin
    if b_origin < 0:
        a = 1 / a
    elif b_origin == 0:
        return 1
    return a
