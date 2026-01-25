#!/usr/bin/python3
"""Module that defines a function to print text with indentation.
The text is printed to standard output, and two new lines are added after
each occurrence of the characters '.', '?' and ':'.
"""


def text_indentation(text):
    """Prints text with indentation.

    Two new lines are printed after each '.', '?' or ':' character found
    in the text.

    Args:
        text (str): the text to be printed

    Raises:
        TypeError: if text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    count = 1

    for c in range(len(text)):
        if count == len(text):
            print(text[c], end="")
            break
        if text[c] in ('.', '?', ':'):
            print("{:s}\n".format(text[c]))
        else:
            print(text[c], end="")
        count += 1
