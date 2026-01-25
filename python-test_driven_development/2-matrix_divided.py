#!/usr/bin/python3
"""
This is the "matrix_divided" module.

The matrix_divided module supplies one function, matrix_divided().

>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number.

    Args:
        matrix: A list of lists of integers or floats
        div: The number to divide by (integer or float)

    Returns:
        A new matrix with all elements divided by div and rounded to 2 decimals

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
        TypeError: If rows of the matrix have different sizes
        TypeError: If div is not a number
        ZeroDivisionError: If div is equal to 0
    """

    if type(div) is bool or type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(error_msg)
    
    for row in matrix:
        if type(row) is not list or len(row) == 0:
            raise TypeError(error_msg)
        for element in row:
            if type(element) is bool or type(element) not in (int, float):
                raise TypeError(error_msg)
    
    first_row_length = len(matrix[0])
    for row in matrix[1:]:
        if len(row) != first_row_length:
            raise TypeError("Each row of the matrix must have the same size")
    
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            result = element / div
            new_row.append(float("{:.2f}".format(result)))
        new_matrix.append(new_row)
    
    return new_matrix
