#!/usr/bin/python3
"""Module for checking if an object is exactly an instance of a class."""


def is_same_class(obj, a_class):
    """Tests if an object is exactly an instance of a specific class.

    Args:
        obj (any): object of any type.
        a_class (class): the class to compare the object with.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.

    """
    return type(obj) is a_class
