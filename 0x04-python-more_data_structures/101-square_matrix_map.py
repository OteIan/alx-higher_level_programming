#!/usr/bin/python3
def square_matrix_map(matrix=[]):  # y -> sub_matrix
    return list(map(lambda y: list(map(lambda x: x ** 2, y)), matrix))
