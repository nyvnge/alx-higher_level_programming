#!/usr/bin/python3
"""This defines a matrix division Function"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: if matrix contains non-numbers
        TypeError: if matrix contains rows of different sizes
        TypeError: if div isn't an int//float
        ZeroDivisionError: if div is 0
    Returns:
        A new matrix representing results of division operation
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Rows of the matrix must have the same size all together")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a no")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
