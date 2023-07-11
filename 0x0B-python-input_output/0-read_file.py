#!/usr/bin/python3
"""Defines a text file-reading function."""

def read_file(filename=""):
    """Prints contents of a text file(UTF-8) to stdout"""
    with open(filename, 'r', encoding = 'utf-8') as f:
        content = f.read()
        print(content, end = "")
