#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        sub_matrix=[]
        for j in range(len(matrix[i])):
            x = matrix[i][j] * matrix[i][j]
            sub_matrix.append(x)
        new_matrix.append(sub_matrix)

    return new_matrix
