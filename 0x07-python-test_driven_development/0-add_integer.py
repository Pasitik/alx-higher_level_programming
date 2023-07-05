#!/usr/bin/python3
"""Contains an add function for integers"""


def add_integer(a, b=98):
    """function for adding two numbers"""

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(a, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        int(a)
    if isinstance(b, float):
        int(b)
    return int(a) + int(b)
