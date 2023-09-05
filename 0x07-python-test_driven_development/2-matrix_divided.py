#!/usr/bin/python3
""" This defines a function that divides all elements of a list """


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor

    Args:
        matrix (List[List[Union[int,float]]]): 2 dimensional list containing
            integers or floats
        div (int): Divisor

    Return:
        list[list[float]]: A new matrix where all elements are divided by 'div,
            rounded to 2 decimal places

    Raises:
        TypeError: If 'matrix' is not a valid matrix of integers/floats,
            or if 'div' is not a number, or if all rows in 'matrix' are not
            of the same length
        ZeroDivisionError: If 'div' is equal to zero
    """
    if matrix is None or div is None:
        return None

    # Checks if 'matrix' is a list of lists containing integers/floats
    if not (isinstance(matrix, list) and
            all(isinstance(row, list) for row in matrix) and
            all(isinstance(value, (int, float))for row in matrix
            for value in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if every row of matrix is of the same length
    first_row_length = len(matrix[0])
    # Starts to iterate through the matrix from the second row
    for row in matrix[1:]:
        # If lengths are different not all are of the same length
        if len(row) != first_row_length:
            raise TypeError("Each row of the matrix must have the same size")
    # Create a deep copy for matrix
    new_matrix = [row[:] for row in matrix]

    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    return list(map(lambda y: list(map(lambda x: round(x/div, 2), y)),
                    new_matrix))
