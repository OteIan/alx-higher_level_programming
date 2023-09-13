#!/usr/bin/python3
"""
This script defines a function 'pascal_triangle' to generate Pascal's Triangle up to the nth row.

Usage:
    To use this script, call the 'pascal_triangle' function with the desired number of rows (n).

Example:
    pascal_triangle(5) returns a list containing Pascal's Triangle up to the 5th row.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows to generate in Pascal's Triangle.

    Returns:
        list of lists: A list containing Pascal's Triangle up to the nth row.
    """
    if n <= 0:
        return []
    
    matrix = []
    for i in range(n):
        temp_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                num = matrix[i-1][j] + matrix[i-1][j-1]
                temp_list.append(num)

        matrix.append(temp_list)
    
    return matrix
