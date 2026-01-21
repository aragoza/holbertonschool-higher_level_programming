#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        return 0, None
    a = 0
    for i in sentence:
        a += 1
    return a, sentence[0]
