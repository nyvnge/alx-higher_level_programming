#!/usr/bin/python3
"""This defines matrix division function"""

def matrix_divided(matrix, divisor):
    """
    Divides a matrix by a scalar integer and returns a new matrix rounded to two decimal places.

    :param matrix: a matrix (list of lists) of integers/floats.
    :param divisor: a scalar integer to divide the matrix.
    :return: a new matrix rounded to two decimal places.

    :raises TypeError: if the matrix is not a list of lists or contains non-numeric elements,
        or if the divisor is not a number.
    :raises ZeroDivisionError: if the divisor is zero.
    :raises TypeError: if the rows of the matrix are not of equal length.
    """

    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(error_msg)

    row_lengths = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error_msg)

        row_lengths.append(len(row))

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error_msg)

    if len(set(row_lengths)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(divisor, (int, float)):
        raise TypeError("divisor must be a number")

    if divisor == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [
        [round(element / divisor, 2) for element in row]
        for row in matrix
    ]

    return new_matrix
