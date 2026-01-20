#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a[0] == None:
        tuple_a[0] = 0
    if tuple_a[1] == None:
        tuple_a[1] = 0
    if tuple_b[0] == None:
        tuple_b[0] = 0
    if tuple_b[1] == None:
        tuple_b[1] = 0

    tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return tuple_c