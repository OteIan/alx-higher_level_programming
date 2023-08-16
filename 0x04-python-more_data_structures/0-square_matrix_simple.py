#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    # Create a deep copy of the matrix list
    new_matrix = [row[:] for row in matrix]
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            new_matrix[i][j] **= 2
    return new_matrix
