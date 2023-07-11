#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    if isinstance(obj, MyClass):
        return{"name": obj.name, "number": obj.number}
