#!/usr/bin/python3

"""
Contains pascal_triangle function
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s
    triangle of n

    Args:
        n (int): integer used to build the pascal triangle
    """
	arr = []
    for row in range(n):
        temp = [1]
        for j in range(row):
            if row == 1:
                temp.append(1)
            else:
                if j == row - 1:
                    temp.append(1)
                else:
                    x = arr[row-1][j] + arr[row-1][j+1]
                    temp.append(x)
        arr.append(temp)
    return (arr)
