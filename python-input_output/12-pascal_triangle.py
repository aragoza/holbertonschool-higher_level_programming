#!/usr/bin/python3

"""
Pascal Triangle
"""


def pascal_triangle(n):
    """
    Docstring for pascal_triangle

    :param n: Description
    """

    if n <= 0:
        return list()

    row = list([1])
    triangle = [[1]]

    for k in range(n-1):
        new_row = [1]
        for j in range(1, len(row)):
            if j == 0:
                new_row.append(row[j])
            elif j == len(new_row):
                new_row.append(row[j-1] + row[j])
            else:
                new_row[j] = row[j-1] + row[j]
        new_row.append(1)
        triangle.append(new_row)
        row = new_row

    return triangle
