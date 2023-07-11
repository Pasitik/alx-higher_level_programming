#!/usr/bin/python3
"""defines a function for writing into a file"""


def write_file(filename="", text=""):
    """writes string to text file (UTF8) & returns number of chars written"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
