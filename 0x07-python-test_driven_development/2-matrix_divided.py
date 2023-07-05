#!/usr/bin/python3
"""
Contains matrix_divided function that divides the elements of a function
by a number
"""


def matrix_divided(matrix, div):
    """returns a new list after dividing each matrix element with div"""

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    isValid = all((isinstance(item, int) or
                   isinstance(item, float)) for row in matrix for item in row)

    lenValid = all(len(row) == len(matrix[0]) for row in matrix)

    if not isValid:
        raise TypeError("matrix must be a matrix
                        (list of lists) of integers/floats")
    if not lenValid:
        raise TypeError("Each row of the matrix must have the same size")
    new_list = []
    for i in range(len(matrix)):
        new_list.append([round(k/div, 2) for k in matrix[i]])

    return new_list
