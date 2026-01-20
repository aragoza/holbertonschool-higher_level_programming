#!/usr/bin/python3

def multiple_returns(sentence):
    a = 0
    for i in sentence:
        a += 1
    return a, sentence[0]
