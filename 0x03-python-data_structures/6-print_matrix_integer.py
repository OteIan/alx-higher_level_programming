#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None or not matrix:
        print("")
        return
    for i in range(len(matrix)):
        if not matrix[i]:
            print("")
        else:
            for j in range(len(matrix[i])):
                if j == len(matrix[i]) - 1:
                    print("{:d}".format(matrix[i][j]))
                else:
                    print("{:d}".format(matrix[i][j]), end=' ')
